%define lua_version 5.1
%define debug_package %{nil}

Name: openresty-lua-balancer
Version: 0.03
Release: 2%{?dist}
Summary: openresty lua balancer
License: BSD
URL: https://github.com/openresty/lua-resty-balancer
Source: %{url}/archive/v%{version}/lua-resty-balancer-v%{version}.tar.gz
BuildRequires: libtool, make
Requires: nginx, lua = %{lua_version}

%description
A generic consistent hash and roundrobin implementations for OpenResty/LuaJIT.

%prep
%setup -q -n lua-resty-balancer-%{version}

%build
cd %{_builddir}/lua-resty-balancer-%{version}
%make_build

%install
%{__install} -d %{buildroot}%{_libdir}/lua/%{lua_version}
%{__install} -d %{buildroot}%{_datadir}/lua/%{lua_version}/resty

%{__install} -m 755 %{_builddir}/lua-resty-balancer-%{version}/*.so \
  %{buildroot}%{_libdir}/lua/%{lua_version}
%{__install} -m 755 %{_builddir}/lua-resty-balancer-%{version}/lib/resty/*.lua \
  %{buildroot}%{_datadir}/lua/%{lua_version}/resty

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/lua/%{lua_version}/*.so
%{_datadir}/lua/%{lua_version}/resty/*.lua
