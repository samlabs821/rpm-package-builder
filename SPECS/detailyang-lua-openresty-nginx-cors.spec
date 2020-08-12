%define detailyang_lua_openresty_nginx_cors_version 0.2.1
%define lua_version 5.1
%define debug_package %{nil}

Summary: detailyang lua openresty nginx cors
Name: detailyang-lua-openresty-nginx-cors
Version: %{detailyang_lua_openresty_nginx_cors_version}
Release: 1%{?dist}
License: BSD
URL: https://github.com/detailyang/lua-resty-cors

Source: https://github.com/detailyang/lua-resty-cors/archive/%{detailyang_lua_openresty_nginx_cors_version}/lua-resty-cors-%{detailyang_lua_openresty_nginx_cors_version}.tar.gz

Requires: nginx, lua = %{lua_version}

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q -n lua-resty-cors-%{detailyang_lua_openresty_nginx_cors_version}

%install
%{__rm} -rf %{buildroot}
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/

%{__install} -Dm755 %{_builddir}/lua-resty-cors-%{detailyang_lua_openresty_nginx_cors_version}/lib/resty/*.lua \
    $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/share/lua/%{lua_version}/resty/*.lua
