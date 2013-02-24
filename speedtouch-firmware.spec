#http://download.ethomson.com/download/WebUpgrade_MacOSX_R3.zip
#http://download.ethomson.com/download/KQD6_R204.zip
#http://www.speedtouch.com/download/drivers/USB/SpeedTouch330_firmware_3012.zip

Name:		speedtouch-firmware
Version: 	0.1
Release: 	9
License: 	Commercial
Group:		System/Kernel and hardware
URL: 		http://speedtouch.sourceforge.net
Source0: 	speedtouch_mgmt-%{version}.tar.bz2
Summary: 	Alcatel Speedtouch USB adsl modem microcode
%rename		speed_touch_mgmt
BuildRequires:	speedtouch-firmware-extractor
BuildArch:	noarch

%description
Alcatel Speedtouch USB adsl modem microcode. Copyright Alcatel.
Needed to make the modem work.

%prep
%setup -q -n speedtouch_mgmt-%{version}
mv mgmt.o mgmt_rev0.o

%build
for rev in 0 2 4; do
  /usr/sbin/firmware-extractor mgmt_rev$rev.o
  for stage in 1 2; do
    mv speedtch-$stage.bin speedtch-$stage.bin.$rev
  done
done

%install
mkdir -p -m755 %{buildroot}/lib/firmware
install -m644 speedtch-*.bin.* %{buildroot}/lib/firmware

%files
/lib/firmware/speedtch-*.bin.*
