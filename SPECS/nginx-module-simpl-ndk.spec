%define simpl_ndk_version 0.3.1
%define nginx_version 1.19.2
%define debug_package %{nil}

Name: nginx-module-simpl-ndk
Version: %{nginx_version}+%{simpl_ndk_version}
Release: 2%{?dist}
Summary: nginx simpl ndk shared module
License: BSD
URL: https://github.com/simpl/ngx_devel_kit
Source0: https://nginx.org/download/nginx-%{nginx_version}.tar.gz
Source1: %{url}/archive/v%{simpl_ndk_version}/ngx_devel_kit-%{simpl_ndk_version}.tar.gz
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
Requires: nginx = 1:%{nginx_version}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The NDK is an Nginx module that is designed to extend the core functionality of the excellent Nginx webserver in a way that can be used as a basis of other Nginx modules.

%prep
%setup -q -n nginx-%{nginx_version}
%setup -T -D -b 1 -q -n ngx_devel_kit-%{simpl_ndk_version}

%build
cd %{_builddir}/nginx-%{nginx_version}
./configure --with-compat --add-dynamic-module=../ngx_devel_kit-%{simpl_ndk_version}
%make_build modules

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_libdir}/nginx/modules
%{__install} -m 755 %{_builddir}/nginx-%{nginx_version}/objs/ndk_http_module.so \
  %{buildroot}%{_libdir}/nginx/modules/ndk_http_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so
