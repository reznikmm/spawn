%undefine _hardened_build
%define _gprdir %_GNAT_project_dir
%define rtl_version 0.1

Name:       spawn
Version:    0.1.0
Release:    git%{?dist}
Summary:    Ada Process API
Group:      Development/Libraries
License:    MIT
URL:        https://github.com/reznikmm/spawn
### Direct download is not availeble
Source0:    spawn.tar.gz
BuildRequires:   gcc-gnat
BuildRequires:   fedora-gnat-project-common  >= 3
BuildRequires:   gprbuild

# gprbuild only available on these:
ExclusiveArch: %GPRbuild_arches

%description
This library provides simple API to spawn processes and communicate with them.

%package devel

Group:      Development/Libraries
License:    MIT
Summary:    Devel package for Ada Pretty
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   fedora-gnat-project-common  >= 2

%description devel
Devel package for spawn

%prep
%setup -q -n %{name}

%build
make  %{?_smp_mflags} GPRBUILD_FLAGS="%Gnatmake_optflags"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} PREFIX=%{_prefix} GPRDIR=%{_gprdir} BINDIR=%{_bindir}

%check
make  %{?_smp_mflags} GPRBUILD_FLAGS="%Gnatmake_optflags" check

%files
%doc LICENSE
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libspawn.so.%{rtl_version}
%{_libdir}/libspawn.so.%{rtl_version}
%{_libdir}/%{name}/libspawn.so.0
%{_libdir}/libspawn.so.0
%files devel
%doc README.md
%{_libdir}/%{name}/libspawn.so
%{_libdir}/libspawn.so
%{_libdir}/%{name}/*.ali
%{_includedir}/%{name}
%{_gprdir}/spawn.gpr
%{_gprdir}/manifests/spawn


%changelog
* Sat Feb 22 2020 Maxim Reznik <reznikmm@gmail.com> - 0.1.0-git
- Initial package
