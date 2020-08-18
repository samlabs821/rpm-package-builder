%define debug_package %{nil}

Name: prometheus
Version: 2.20.1
Release: 4%{?dist}
Summary: monitoring system and time series database
License: ASL 2.0
URL: https://prometheus.io
Source: https://github.com/prometheus/prometheus/releases/download/v%{version}/prometheus-%{version}.linux-amd64.tar.gz
%{?systemd_requires}
Requires(pre): shadow-utils

%description
Prometheus, a Cloud Native Computing Foundation project, is a systems and service monitoring system.
It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts if some condition is observed to be true.

%prep
%setup -q -n prometheus-%{version}.linux-amd64

%install
%{__install} -d %{buildroot}%{_sharedstatedir}/prometheus
%{__install} -d %{buildroot}%{_datadir}/prometheus/consoles
%{__install} -d %{buildroot}%{_datadir}/prometheus/console_libraries
%{__install} -d %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_sysconfdir}/default
%{__install} -d %{buildroot}%{_sysconfdir}/prometheus
%{__install} -d %{buildroot}%{_unitdir}
%{__install} -m 755 prometheus %{buildroot}%{_bindir}/prometheus
%{__install} -m 755 promtool %{buildroot}%{_bindir}/promtool
%{__install} -m 755 tsdb %{buildroot}%{_bindir}/tsdb
%{__install} -m 644 consoles/* %{buildroot}%{_datarootdir}/prometheus/consoles
%{__install} -m 644 console_libraries/* %{buildroot}%{_datarootdir}/prometheus/consoles
%{__install} -m 644 prometheus.yml %{buildroot}%{_sysconfdir}/prometheus/prometheus.yml
cat <<EOF > %{buildroot}%{_unitdir}/prometheus.service
[Unit]
Description=Monitoring system and time series database
Documentation=https://prometheus.io/docs/introduction/overview

[Service]
Restart=always
User=prometheus
Group=prometheus
EnvironmentFile=%{_sysconfdir}/default/prometheus
ExecStart=%{_bindir}/prometheus \$ARGS
ExecReload=%{_bindir}/kill -HUP \$MAINPID
SendSIGKILL=no

[Install]
WantedBy=multi-user.target
EOF
cat <<EOF > %{buildroot}%{_sysconfdir}/default/prometheus
ARGS="--config.file=%{_sysconfdir}/prometheus/prometheus.yml \
  --storage.tsdb.path=%{_sharedstatedir}/prometheus/data \
  --web.console.libraries=%{_datarootdir}/prometheus/console_libraries \
  --web.console.templates=%{_datarootdir}/prometheus/consoles"
EOF

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
  useradd -r -g prometheus -d %{_sharedstatedir}/prometheus -s /sbin/nologin \
          -c "Prometheus daemon" prometheus
exit 0

%post
%systemd_post prometheus.service

%preun
%systemd_preun prometheus.service

%postun
%systemd_postun prometheus.service

%files
%defattr(-,root,root,-)
%{_bindir}/prometheus
%{_bindir}/promtool
%{_bindir}/tsdb
%config(noreplace) %{_sysconfdir}/prometheus/prometheus.yml
%{_datarootdir}/prometheus
%{_unitdir}/prometheus.service
%config(noreplace) %{_sysconfdir}/default/prometheus
%dir %attr(755, prometheus, prometheus)%{_sharedstatedir}/prometheus
