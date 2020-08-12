%define openresty_stream_lua_version 0.0.8
%define nginx_version 1.19.2
%define debug_package %{nil}

Summary: nginx openresty stream lua shared module
Name: nginx-module-openresty-stream-lua
Version: %{nginx_version}+%{openresty_stream_lua_version}
Release: 1%{?dist}
Vendor: damex
URL: https://github.com/openresty/stream-lua-nginx-module
License: BSD

Source0: https://nginx.org/download/nginx-%{nginx_version}.tar.gz
Source1: https://github.com/openresty/stream-lua-nginx-module/archive/v%{openresty_stream_lua_version}/stream-lua-v%{openresty_stream_lua_version}.tar.gz

Requires: nginx = 1:%{nginx_version}
Requires: nginx-module-simpl-ndk
Requires: luajit
BuildRequires: luajit-devel
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q -n nginx-%{nginx_version}
%setup -T -D -b 1 -n stream-lua-nginx-module-%{openresty_stream_lua_version}

%build
cd %{_builddir}/nginx-%{nginx_version}
export LUAJIT_INC=/usr/include/luajit-2.0
export LUAJIT_LIB=%{_libdir}
./configure --with-compat --with-stream --with-stream_ssl_module --add-dynamic-module=../stream-lua-nginx-module-%{openresty_stream_lua_version}
make modules

%install
%{__rm} -rf %{buildroot}

%{__install} -Dm755 %{_builddir}/nginx-%{nginx_version}/objs/ngx_stream_lua_module.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_stream_lua_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so
