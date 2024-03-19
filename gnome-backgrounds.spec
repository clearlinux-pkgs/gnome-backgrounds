#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v4
# autospec commit: f4bef72
#
Name     : gnome-backgrounds
Version  : 46.0
Release  : 29
URL      : https://download.gnome.org/sources/gnome-backgrounds/46/gnome-backgrounds-46.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-backgrounds/46/gnome-backgrounds-46.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-SA-3.0
Requires: gnome-backgrounds-data = %{version}-%{release}
Requires: gnome-backgrounds-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gettext
BuildRequires : itstool
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# GNOME Backgrounds
This module contains a set of backgrounds packaged with the GNOME desktop.

%package data
Summary: data components for the gnome-backgrounds package.
Group: Data

%description data
data components for the gnome-backgrounds package.


%package license
Summary: license components for the gnome-backgrounds package.
Group: Default

%description license
license components for the gnome-backgrounds package.


%prep
%setup -q -n gnome-backgrounds-46.0
cd %{_builddir}/gnome-backgrounds-46.0
pushd ..
cp -a gnome-backgrounds-46.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710889959
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-backgrounds
cp %{_builddir}/gnome-backgrounds-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-backgrounds/2995e7d53219d710383087253fb9a1e760e44f35 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/backgrounds/gnome/adwaita-d.jxl
/usr/share/backgrounds/gnome/adwaita-l.jxl
/usr/share/backgrounds/gnome/amber-d.jxl
/usr/share/backgrounds/gnome/amber-l.jxl
/usr/share/backgrounds/gnome/blobs-d.svg
/usr/share/backgrounds/gnome/blobs-l.svg
/usr/share/backgrounds/gnome/drool-d.svg
/usr/share/backgrounds/gnome/drool-l.svg
/usr/share/backgrounds/gnome/fold-d.jxl
/usr/share/backgrounds/gnome/fold-l.jxl
/usr/share/backgrounds/gnome/geometrics-d.jxl
/usr/share/backgrounds/gnome/geometrics-l.jxl
/usr/share/backgrounds/gnome/glass-chip-d.jxl
/usr/share/backgrounds/gnome/glass-chip-l.jxl
/usr/share/backgrounds/gnome/morphogenesis-d.svg
/usr/share/backgrounds/gnome/morphogenesis-l.svg
/usr/share/backgrounds/gnome/neogeo-d.jxl
/usr/share/backgrounds/gnome/neogeo-l.jxl
/usr/share/backgrounds/gnome/pills-d.jxl
/usr/share/backgrounds/gnome/pills-l.jxl
/usr/share/backgrounds/gnome/pixels-d.jpg
/usr/share/backgrounds/gnome/pixels-l.jpg
/usr/share/backgrounds/gnome/ring-d.jxl
/usr/share/backgrounds/gnome/ring-l.jxl
/usr/share/backgrounds/gnome/symbolic-d.png
/usr/share/backgrounds/gnome/symbolic-l.png
/usr/share/backgrounds/gnome/tarka-d.jxl
/usr/share/backgrounds/gnome/tarka-l.jxl
/usr/share/backgrounds/gnome/vnc-d.png
/usr/share/backgrounds/gnome/vnc-l.png
/usr/share/gnome-background-properties/adwaita.xml
/usr/share/gnome-background-properties/amber.xml
/usr/share/gnome-background-properties/blobs.xml
/usr/share/gnome-background-properties/drool.xml
/usr/share/gnome-background-properties/fold.xml
/usr/share/gnome-background-properties/geometrics.xml
/usr/share/gnome-background-properties/glass-chip.xml
/usr/share/gnome-background-properties/morphogenesis.xml
/usr/share/gnome-background-properties/neogeo.xml
/usr/share/gnome-background-properties/pills.xml
/usr/share/gnome-background-properties/pixels.xml
/usr/share/gnome-background-properties/ring.xml
/usr/share/gnome-background-properties/symbolic.xml
/usr/share/gnome-background-properties/tarka.xml
/usr/share/gnome-background-properties/vnc.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-backgrounds/2995e7d53219d710383087253fb9a1e760e44f35
