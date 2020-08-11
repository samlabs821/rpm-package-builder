%define openresty_lua_balancer 0.03
%define lua_version 5.1
%define debug_package %{nil}

Summary: openresty lua balancer
Name: openresty-lua-balancer
Version: %{openresty_lua_balancer}
Release: 1%{?dist}
License: BSD
Vendor: damex
URL: https://github.com/openresty/lua-resty-balancer

Source: https://github.com/openresty/lua-resty-balancer/archive/v%{openresty_lua_balancer}/lua-resty-balancer-v%{openresty_lua_balancer}.tar.gz

Requires: nginx, lua = %{lua_version}
BuildRequires: libtool
BuildRequires: make

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q -n lua-resty-balancer-%{openresty_lua_balancer}

%build
cd %{_builddir}/lua-resty-balancer-%{openresty_lua_balancer}
make

%install
%{__rm} -rf %{buildroot}
%{__install} -d $RPM_BUILD_ROOT%{_libdir}/lua/%{lua_version}
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/

%{__install} -Dm755 %{_builddir}/lua-resty-balancer-%{openresty_lua_balancer}/*.so \
    $RPM_BUILD_ROOT%{_libdir}/lua/%{lua_version}
%{__install} -Dm755 %{_builddir}/lua-resty-balancer-%{openresty_lua_balancer}/lib/resty/*.lua \
    $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/lua/%{lua_version}/*.so
/usr/share/lua/%{lua_version}/resty/*.lua
