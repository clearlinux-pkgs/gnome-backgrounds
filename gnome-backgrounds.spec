#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-backgrounds
Version  : 3.24.0
Release  : 1
URL      : https://download.gnome.org/sources/gnome-backgrounds/3.24/gnome-backgrounds-3.24.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-backgrounds/3.24/gnome-backgrounds-3.24.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-backgrounds-data
Requires: gnome-backgrounds-locales
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)

%description
gnome-backgrounds
=================
This module contains a set of backgrounds packaged with the GNOME desktop.

%package data
Summary: data components for the gnome-backgrounds package.
Group: Data

%description data
data components for the gnome-backgrounds package.


%package locales
Summary: locales components for the gnome-backgrounds package.
Group: Default

%description locales
locales components for the gnome-backgrounds package.


%prep
%setup -q -n gnome-backgrounds-3.24.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491770898
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491770898
rm -rf %{buildroot}
%make_install
%find_lang gnome-backgrounds

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/backgrounds/gnome/Bokeh_Tails.jpg
/usr/share/backgrounds/gnome/Chmiri.jpg
/usr/share/backgrounds/gnome/Dark_Ivy.jpg
/usr/share/backgrounds/gnome/Fabric.jpg
/usr/share/backgrounds/gnome/Flowerbed.jpg
/usr/share/backgrounds/gnome/Godafoss_Iceland.jpg
/usr/share/backgrounds/gnome/Icescape.jpg
/usr/share/backgrounds/gnome/Mirror.jpg
/usr/share/backgrounds/gnome/Road.jpg
/usr/share/backgrounds/gnome/Sandstone.jpg
/usr/share/backgrounds/gnome/Stones.jpg
/usr/share/backgrounds/gnome/Terraform-green.jpg
/usr/share/backgrounds/gnome/Waterfalls.jpg
/usr/share/backgrounds/gnome/Waves.jpg
/usr/share/backgrounds/gnome/adwaita-day.jpg
/usr/share/backgrounds/gnome/adwaita-lock.jpg
/usr/share/backgrounds/gnome/adwaita-morning.jpg
/usr/share/backgrounds/gnome/adwaita-night.jpg
/usr/share/backgrounds/gnome/adwaita-timed.xml
/usr/share/gnome-background-properties/adwaita.xml
/usr/share/gnome-background-properties/gnome-backgrounds.xml

%files locales -f gnome-backgrounds.lang
%defattr(-,root,root,-)

