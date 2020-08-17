%define openresty_http_lua_version 0.10.17
%define nginx_version 1.19.2
%define debug_package %{nil}

Name: nginx-module-openresty-http-lua
Version: %{nginx_version}+%{openresty_http_lua_version}
Release: 3%{?dist}
Summary: nginx openresty http lua shared module
License: BSD
URL: https://github.com/openresty/lua-nginx-module
Source0: https://nginx.org/download/nginx-%{nginx_version}.tar.gz
Source1: %{url}/archive/v%{openresty_http_lua_version}/http-lua-%{openresty_http_lua_version}.tar.gz
BuildRequires: luajit-devel, libtool, autoconf, automake, make, openssl-devel, pcre-devel, zlib-devel
Requires: nginx = 1:%{nginx_version}, nginx-module-simpl-ndk, luajit

%description
This module embeds LuaJIT 2.0/2.1 into Nginx. It is a core component of OpenResty.

%prep
%setup -q -n nginx-%{nginx_version}
%setup -T -D -b 1 -n lua-nginx-module-%{openresty_http_lua_version}

%build
cd %{_builddir}/nginx-%{nginx_version}
export LUAJIT_INC=%{_includedir}/luajit-2.0
export LUAJIT_LIB=%{_libdir}
./configure --with-ld-opt="-Wl,-rpath,$LUAJIT_LIB" --with-compat --add-dynamic-module=../lua-nginx-module-%{openresty_http_lua_version}
%make_build modules

%install
%{__install} -d %{buildroot}%{_libdir}/nginx/modules

%{__install} -m 755 %{_builddir}/nginx-%{nginx_version}/objs/ngx_http_lua_module.so \
  %{buildroot}%{_libdir}/nginx/modules/ngx_http_lua_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so
