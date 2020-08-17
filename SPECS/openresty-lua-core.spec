%define lua_version 5.1
%define debug_package %{nil}

Name: openresty-lua-core
Version: 0.1.19
Release: 2%{?dist}
Summary: openresty lua core
License: BSD
URL: https://github.com/openresty/lua-resty-core
Source: %{url}/archive/v%{version}/lua-resty-core-v%{version}.tar.gz
Requires: nginx, lua = %{lua_version}
BuildArch: noarch

%description
New FFI-based Lua API for ngx_http_lua_module and/or ngx_stream_lua_module.

%prep
%setup -q -n lua-resty-core-%{version}

%install
%{__install} -d %{buildroot}%{_datadir}/lua/%{lua_version}/resty
%{__install} -d %{buildroot}%{_datadir}/lua/%{lua_version}/resty/core
%{__install} -d %{buildroot}%{_datadir}/lua/%{lua_version}/ngx
%{__install} -d %{buildroot}%{_datadir}/lua/%{lua_version}/ngx/ssl

%{__install} -m 755 %{_builddir}/lua-resty-core-%{version}/lib/resty/*.lua \
  %{buildroot}%{_datadir}/lua/%{lua_version}/resty
%{__install} -m 755 %{_builddir}/lua-resty-core-%{version}/lib/resty/core/*.lua \
  %{buildroot}%{_datadir}/lua/%{lua_version}/resty/core
%{__install} -m 755 %{_builddir}/lua-resty-core-%{version}/lib/ngx/*.lua \
  %{buildroot}%{_datadir}/lua/%{lua_version}/ngx
%{__install} -m 755 %{_builddir}/lua-resty-core-%{version}/lib/ngx/ssl/*.lua \
  %{buildroot}%{_datadir}/lua/%{lua_version}/ngx/ssl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/lua/%{lua_version}/resty/*.lua
%{_datadir}/lua/%{lua_version}/resty/core/*.lua
%{_datadir}/lua/%{lua_version}/ngx/*.lua
%{_datadir}/lua/%{lua_version}/ngx/ssl/*.lua
