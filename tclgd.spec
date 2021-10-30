%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tclgd
Summary:       Tcl interface to GD graphics drawing library
Version:       1.3.1
Release:       0
License:       BSD-3-Clause
Group:         Development/Libraries/Tcl
Source:        tcl.gd-%{version}.tar.gz
URL:           https://github.com/flightaware/tcl.gd
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.6
BuildRequires: gd-devel
%if 0%{?suse_version} >= 1500
BuildRequires: freetype2-devel
BuildRequires: fontconfig-devel
BuildRequires: libXpm-devel
BuildRequires: libX11-devel
%endif
Requires:      tcl >= 8.6
Requires:      gd
BuildRoot:     %{buildroot}

%description
This is tclgd, a new Tcl interface to GD that is significantly more feature-
complete with gd 2 than Gdtclft.

%package devel
Summary:        Development package for tclgd
Group:          Development/Libraries/Tcl
Requires:       %{name} = %version

%description devel
This package contains development files for tclgd.

%prep
%setup -q -n tcl.gd-%{version}

%build
autoconf
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib}
make 

%check
make test

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}
/usr/share/man/mann

%files devel
%defattr(-,root,root)
%{directory}/include/*.h

