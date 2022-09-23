#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-backgrounds
Version  : 43
Release  : 22
URL      : https://download.gnome.org/sources/gnome-backgrounds/43/gnome-backgrounds-43.tar.xz
Source0  : https://download.gnome.org/sources/gnome-backgrounds/43/gnome-backgrounds-43.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-SA-3.0
Requires: gnome-backgrounds-data = %{version}-%{release}
Requires: gnome-backgrounds-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gettext
BuildRequires : itstool

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
%setup -q -n gnome-backgrounds-43
cd %{_builddir}/gnome-backgrounds-43

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663949868
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-backgrounds
cp %{_builddir}/gnome-backgrounds-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-backgrounds/2995e7d53219d710383087253fb9a1e760e44f35 || :
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/backgrounds/gnome/adwaita-d.webp
/usr/share/backgrounds/gnome/adwaita-l.webp
/usr/share/backgrounds/gnome/blobs-d.svg
/usr/share/backgrounds/gnome/blobs-l.svg
/usr/share/backgrounds/gnome/drool-d.svg
/usr/share/backgrounds/gnome/drool-l.svg
/usr/share/backgrounds/gnome/dune-d.svg
/usr/share/backgrounds/gnome/dune-l.svg
/usr/share/backgrounds/gnome/field-d.svg
/usr/share/backgrounds/gnome/field-l.svg
/usr/share/backgrounds/gnome/grid-d.webp
/usr/share/backgrounds/gnome/grid-l.webp
/usr/share/backgrounds/gnome/licorice-d.webp
/usr/share/backgrounds/gnome/licorice-l.webp
/usr/share/backgrounds/gnome/oceans.svg
/usr/share/backgrounds/gnome/pixels-d.webp
/usr/share/backgrounds/gnome/pixels-l.webp
/usr/share/backgrounds/gnome/symbolic-d.webp
/usr/share/backgrounds/gnome/symbolic-l.webp
/usr/share/backgrounds/gnome/truchet-d.webp
/usr/share/backgrounds/gnome/truchet-l.webp
/usr/share/backgrounds/gnome/vnc-d.webp
/usr/share/backgrounds/gnome/vnc-l.webp
/usr/share/backgrounds/gnome/wood-d.webp
/usr/share/backgrounds/gnome/wood-l.webp
/usr/share/gnome-background-properties/adwaita.xml
/usr/share/gnome-background-properties/blobs.xml
/usr/share/gnome-background-properties/drool.xml
/usr/share/gnome-background-properties/dune.xml
/usr/share/gnome-background-properties/field.xml
/usr/share/gnome-background-properties/grid.xml
/usr/share/gnome-background-properties/licorice.xml
/usr/share/gnome-background-properties/oceans.xml
/usr/share/gnome-background-properties/pixels.xml
/usr/share/gnome-background-properties/symbolic.xml
/usr/share/gnome-background-properties/truchet.xml
/usr/share/gnome-background-properties/vnc.xml
/usr/share/gnome-background-properties/wood.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-backgrounds/2995e7d53219d710383087253fb9a1e760e44f35
