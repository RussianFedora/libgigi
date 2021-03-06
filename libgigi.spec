%global svnrev 1044

Name:           libgigi
Version:        0.8.0
Release:        5.svn%{svnrev}%{?dist}.R
Summary:        GiGi (aka GG) is a C++ OpenGL GUI library.

License:        LGPL
URL:            http://gigi.sourceforge.net/

# svn export -r 1044 https://gigi.svn.sourceforge.net/svnroot/gigi/trunk/GG libgigi-0.8.0-svn1044
# tar -czvf libgigi-0.8.0-svn1044.tar.gz libgigi-0.8.0-svn1044/
Source0:        %{name}-%{version}-svn%{svnrev}.tar.gz

Patch1:         libgigi-compile-fix.patch
Patch2:         libgigi-io-fix.patch
Patch3:		libgigi-path-fix.patch

BuildRequires:  boost-devel SDL-devel doxygen ogre-devel libtiff-devel
BuildRequires:  freetype-devel libstdc++-devel gcc-c++ glibc-headers glibc-devel
BuildRequires:  ois-devel DevIL-devel libpng-devel libjpeg-devel

%package devel
Requires:       %{name} = %{version}
Summary:        Development files for libgigi (GiGi/GG)

%package ogre
Requires:       %{name} =  %{version} ogre
Summary:        Ogre plugin for libgigi (GiGi/GG)

%package SDL
Requires:       %{name} =  %{version}
Summary:        SDL plugin for libgigi (GiGi/GG)

%package SDL-devel
Requires:       %{name}-SDL = %{version} %{name}-SDL = %{version}
Summary:        Development files for libgigi(GiGi/GG) SDL plugin

%package ogre-devel
Requires:       %{name}-ogre = %{version}
Summary:        Development files for libgigi(GiGi/GG) Ogre plugin

%package doc
Summary:        Documentation for libgigi(GiGi/GG)
BuildArch:      noarch

%description
GiGi (aka GG) is a C++ OpenGL GUI library.  It has drivers that work with SDL 
(http://www.libsdl.org) and Ogre (http://www.ogre3d.org).

%description doc
Documentation for libgigi(GiGi/GG)

%description devel
Development files for libgigi (GiGi/GG)

%description SDL
SDL plugin for libgigi (GiGi/GG)

%description ogre
Ogre plugin for libgigi (GiGi/GG)

%description SDL-devel
Development files libgigi(GiGi/GG) SDL plugin

%description ogre-devel
Development files for libgigi(GiGi/GG) Ogre plugin

%prep
%setup -q -n %{name}-%{version}-svn%{svnrev}
%patch1 -p1 -b .fix-compile-errors
%patch2 -p1 -b .io-fix-error
%patch3 -p1 -b .path-fix

%build
%cmake .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README
%{_libdir}/libGiGi.so

%files doc
%doc doc/%{name}-%{version}/*

%files SDL
%{_libdir}/libGiGiSDL.so

%files ogre
%{_libdir}/libGiGiOgre.so
%{_libdir}/libGiGiOgrePlugin_OIS.so

%files devel
%{_includedir}/GG/*.h
%{_includedir}/GG/*.py*
%{_includedir}/GG/adobe/*
%{_includedir}/GG/dialogs/*
%{_includedir}/GG/utf8/*
%{_libdir}/pkgconfig/GiGi.pc

%files SDL-devel
%{_includedir}/GG/SDL/SDLGUI.h
%{_libdir}/pkgconfig/GiGiSDL.pc

%files ogre-devel
%{_includedir}/GG/Ogre/*
%{_libdir}/pkgconfig/GiGiOgre.pc

%changelog
* Mon Jan 23 2012 Aleksandra Bookwar <alpha@bookwar.info> - 0.8.0-5.svn1044.R
- Added global svnrev variable

* Mon Jan 23 2012 Aleksandra Bookwar <alpha@bookwar.info> - 0.8.0-4.svn1044.R
- Update to the svn revision 1044

* Mon Aug  1 2011 Alexei Panov <elemc AT atisserv DOT ru> - 0.8.0-3.R
- update for new ogre-library
* Thu Jul 28 2011 Alexei Panov <elemc AT atisserv DOT ru> - 0.8.0-2.R
- added missing build requires (libpng, DevIL, libjpeg)
* Wed Jul 27 2011 Alexei Panov <elemc AT atisserv DOT ru> - 0.8.0-1
- Initial build
