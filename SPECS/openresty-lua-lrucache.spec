%define openresty_lua_lrucache_version 0.10
%define lua_version 5.1
%define debug_package %{nil}

Summary: openresty lua lrucache
Name: openresty-lua-lrucache
Version: %{openresty_lua_lrucache_version}
Release: 1%{?dist}
License: BSD
URL: https://github.com/openresty/lua-resty-lrucache

Source: https://github.com/openresty/lua-resty-lrucache/archive/v%{openresty_lua_lrucache_version}/lua-resty-lrucache-v%{openresty_lua_lrucache_version}.tar.gz

Requires: nginx, lua = %{lua_version}

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q -n lua-resty-lrucache-%{openresty_lua_lrucache_version}

%install
%{__rm} -rf %{buildroot}
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/lrucache

%{__install} -Dm755 %{_builddir}/lua-resty-lrucache-%{openresty_lua_lrucache_version}/lib/resty/*.lua \
    $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty
%{__install} -Dm755 %{_builddir}/lua-resty-lrucache-%{openresty_lua_lrucache_version}/lib/resty/lrucache/*.lua \
    $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}/resty/lrucache

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/share/lua/%{lua_version}/resty/*.lua
/usr/share/lua/%{lua_version}/resty/lrucache/*.lua
