%define name speedtouch-firmware
%define oldname speedtouch_mgmt
%define version 0.1
%define release %mkrel 6
#http://download.ethomson.com/download/WebUpgrade_MacOSX_R3.zip
#http://download.ethomson.com/download/KQD6_R204.zip
#http://www.speedtouch.com/download/drivers/USB/SpeedTouch330_firmware_3012.zip
%define url http://speedtouch.sourceforge.net

Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	Commercial
Group:		System/Kernel and hardware
URL: 		%{url}
Source0: 	%{oldname}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
Summary: 	Alcatel Speedtouch USB adsl modem microcode
Provides:	%{oldname}
Obsoletes:	%{oldname}
BuildRequires:	speedtouch-firmware-extractor
BuildArch:	noarch

%description
Alcatel Speedtouch USB adsl modem microcode. Copyright Alcatel.
Needed to make the modem work.

%prep
%setup -q -n %{oldname}-%{version}
mv mgmt.o mgmt_rev0.o

%build
for rev in 0 2 4; do
  /usr/sbin/firmware-extractor mgmt_rev$rev.o
  for stage in 1 2; do
    mv speedtch-$stage.bin speedtch-$stage.bin.$rev
  done
done

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p -m 755 $RPM_BUILD_ROOT/lib/firmware
install -m 644 speedtch-*.bin.* $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/lib/firmware/speedtch-*.bin.*

