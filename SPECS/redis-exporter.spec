%define debug_package %{nil}

Name: redis-exporter
Version: 1.11.1
Release: 1%{?dist}
Summary: Prometheus Redis Metrics Exporter
License: ASL 2.0
URL: https://github.com/oliver006/redis_exporter
Source: https://github.com/oliver006/redis_exporter/releases/download/v%{version}/redis_exporter-v%{version}.linux-amd64.tar.gz
%{?systemd_requires}
Requires(pre): redis
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Prometheus exporter for Redis metrics.
Supports Redis 2.x, 3.x, 4.x, 5.x, and 6.x

%prep
%setup -q -n redis_exporter-v%{version}.linux-amd64

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_unitdir}
%{__install} -d %{buildroot}%{_sysconfdir}/default
%{__install} -m 755 redis_exporter %{buildroot}%{_bindir}/redis_exporter
cat <<EOF > %{buildroot}%{_unitdir}/redis-exporter.service
[Unit]
Description=Prometheus Redis Metrics Exporter
Documentation=https://github.com/oliver006/redis_exporter

[Service]
Restart=always
User=redis-exporter
Group=redis-exporter
EnvironmentFile=%{_sysconfdir}/default/redis_exporter
ExecStart=%{_bindir}/redis_exporter
ExecReload=%{_bindir}/kill -HUP \$MAINPID
SendSIGKILL=no

[Install]
WantedBy=multi-user.target
EOF
cat <<EOF > %{buildroot}%{_sysconfdir}/default/redis_exporter
REDIS_ADDR="localhost:6379"
REDIS_PASSWORD=""
EOF

%pre
getent group redis-exporter >/dev/null || groupadd -r redis-exporter
getent passwd redis-exporter >/dev/null || \
  useradd -r -g redis-exporter -s /sbin/nologin \
          -c "redis exporter" redis-exporter
exit 0

%post
%systemd_post redis-exporter.service

%preun
%systemd_preun redis-exporter.service

%postun
%systemd_postun redis-exporter.service

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/redis_exporter
%{_unitdir}/redis-exporter.service
%config(noreplace) %{_sysconfdir}/default/redis_exporter
