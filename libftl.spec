Name:           libftl
Version:        0.10.1
Release:        7%{?dist}
Summary:        FTL audio/video streaming library

License:        MIT
URL:            https://github.com/Scrumplex/ftl-sdk
Source0:        https://github.com/Scrumplex/ftl-sdk/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jansson-devel
BuildRequires:  libcurl-devel

%description
FTL-SDK is a cross platform SDK written in C to enable sending audio/video to
mixer using FTL service.


%prep
%autosetup -n ftl-sdk-%{version} 

%package devel
Summary:        Development files for libftl
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for libftl.


%build
mkdir -p build
%cmake -B build \
	-DCMAKE_BUILD_TYPE='Release' \
	-Wno-dev
%make_build -C build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.0*


%files devel
%{_libdir}/pkgconfig/libftl.pc
%{_libdir}/%{name}.so
%{_includedir}/libftl/

%changelog

* Thu Aug 12 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.10.1-7
- Initial build
