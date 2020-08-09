%define openresty_lua_core_version 0.1.19
%define lua_version 5.1
%define debug_package %{nil}

Summary: openresty lua core
Name: openresty-lua-core
Version: %{openresty_lua_core_version}
Release: 1%{?dist}
License: BSD
URL: https://github.com/openresty/lua-resty-core

Source: https://github.com/openresty/lua-resty-core/archive/v%{openresty_lua_core_version}/lua-resty-core-v%{openresty_lua_core_version}.tar.gz

Requires: nginx, lua = %{lua_version}

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q -n lua-resty-core-%{openresty_lua_core_version}

%install
%{__rm} -rf %{buildroot}
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/core
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/ngx/
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/ngx/ssl

%{__install} -Dm755 %{_builddir}/lua-resty-core-%{openresty_lua_core_version}/lib/resty/*.lua \
    $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty
%{__install} -Dm755 %{_builddir}/lua-resty-core-%{openresty_lua_core_version}/lib/resty/core/*.lua \
    $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/core
%{__install} -Dm755 %{_builddir}/lua-resty-core-%{openresty_lua_core_version}/lib/ngx/*.lua \
    $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/ngx
%{__install} -Dm755 %{_builddir}/lua-resty-core-%{openresty_lua_core_version}/lib/ngx/ssl/*.lua \
    $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/ngx/ssl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/share/lua/%{lua_version}/resty/*.lua
/usr/share/lua/%{lua_version}/resty/core/*.lua
/usr/share/lua/%{lua_version}/ngx/*.lua
/usr/share/lua/%{lua_version}/ngx/ssl/*.lua
