%define simpl_ndk_version 0.3.1
%define nginx_version 1.18.0
%define debug_package %{nil}

Summary: nginx simpl ndk shared module
Name: nginx-module-simpl-ndk
Version: %{nginx_version}+%{simpl_ndk_version}
Release: 1%{?dist}
License: BSD
URL: https://github.com/simpl/ngx_devel_kit

Source0: https://nginx.org/download/nginx-%{nginx_version}.tar.gz
Source1: https://github.com/simpl/ngx_devel_kit/archive/v%{simpl_ndk_version}/ngx_devel_kit-%{simpl_ndk_version}.tar.gz

Requires: nginx = 1:%{nginx_version}
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
%setup -T -D -b 1 -n ngx_devel_kit-%{simpl_ndk_version}

%build
cd %{_builddir}/nginx-%{nginx_version}
./configure --with-compat --add-dynamic-module=../ngx_devel_kit-%{simpl_ndk_version}
make modules

%install
%{__rm} -rf %{buildroot}

%{__install} -Dm755 %{_builddir}/nginx-%{nginx_version}/objs/ndk_http_module.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ndk_http_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so
