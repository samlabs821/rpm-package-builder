%define openresty_lua_upstream_healthcheck 0.06
%define lua_version 5.1
%define debug_package %{nil}

Summary: openresty lua upstream healthcheck
Name: openresty-lua-upstream-healthcheck
Version: %{openresty_lua_upstream_healthcheck}
Release: 1%{?dist}
License: BSD
URL: https://github.com/openresty/lua-resty-upstream-healthcheck

Source: https://github.com/openresty/lua-resty-upstream-healthcheck/archive/v%{openresty_lua_upstream_healthcheck}/lua-resty-upstream-healthcheck-v%{openresty_lua_upstream_healthcheck}.tar.gz

Requires: nginx, lua = %{lua_version}

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q -n lua-resty-upstream-healthcheck-%{openresty_lua_upstream_healthcheck}

%install
%{__rm} -rf %{buildroot}
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/upstream/

%{__install} -Dm755 %{_builddir}/lua-resty-upstream-healthcheck-%{openresty_lua_upstream_healthcheck}/lib/resty/upstream/*.lua \
    $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/upstream

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/share/lua/%{lua_version}/resty/upstream/*.lua
