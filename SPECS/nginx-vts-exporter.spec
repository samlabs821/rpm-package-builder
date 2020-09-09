%define debug_package %{nil}

Name: nginx-vts-exporter
Version: 0.10.7
Release: 2%{?dist}
Summary: Simple server that scrapes Nginx vts stats and exports them via HTTP for Prometheus consumption
License: MIT
URL: https://github.com/hnlq715/nginx-vts-exporter
Source: %{url}/archive/v%{version}/nginx-vts-exporter-v%{version}.tar.gz
%{?systemd_requires}
Requires(pre): shadow-utils
BuildRequires: golang
BuildRequires: make
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Simple server that scrapes Nginx vts stats and exports them via HTTP for Prometheus consumption

%prep
%setup -q -n nginx-vts-exporter-%{version}

%build
go get
go build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_sharedstatedir}/prometheus
%{__install} -d %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_sysconfdir}/default
%{__install} -d %{buildroot}%{_unitdir}
%{__install} -m 755 nginx-vts-exporter %{buildroot}%{_bindir}/nginx-vts-exporter
cat <<EOF > %{buildroot}%{_unitdir}/nginx-vts-exporter.service
[Unit]
Description=%{summary}
Documentation=%{url}

[Service]
Restart=always
User=prometheus
Group=prometheus
EnvironmentFile=%{_sysconfdir}/default/nginx-vts-exporter
ExecStart=%{_bindir}/nginx-vts-exporter \$ARGS
ExecReload=%{_bindir}/kill -HUP \$MAINPID
SendSIGKILL=no

[Install]
WantedBy=multi-user.target
EOF
cat <<EOF > %{buildroot}%{_sysconfdir}/default/nginx-vts-exporter
ARGS="-nginx.scrape_uri=http://localhost/status/format/json"
EOF

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
  useradd -r -g prometheus -d %{_sharedstatedir}/prometheus -s /sbin/nologin \
          -c "Prometheus daemon" prometheus
exit 0

%post
%systemd_post nginx-vts-exporter.service

%preun
%systemd_preun nginx-vts-exporter.service

%postun
%systemd_postun nginx-vts-exporter.service

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/nginx-vts-exporter
%{_unitdir}/nginx-vts-exporter.service
%config(noreplace) %{_sysconfdir}/default/nginx-vts-exporter
%dir %attr(755, prometheus, prometheus)%{_sharedstatedir}/prometheus
