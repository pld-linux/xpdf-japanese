Summary:	ISO-2022-JP, EUC-JP and Shift-JIS encoding support for xpdf
Summary(pl):	Wsparcie kodowania ISO-2022-JP, EUC-JP i Shift-JIS dla xpdf
Name:		xpdf-japanese
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}.tar.gz
# Source0-md5:	7f3d680a49fd71cb86c0d60527402217
URL:		http://www.foolabs.com/xpdf/
Requires(post,preun):	grep
Requires(post,preun):	xpdf
Requires(preun):	fileutils
Requires:	xpdf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.) 
This package provides support files needed to use the Xpdf tools with
Japanese PDF files.

%description -l pl
Pakiety wspieraj�ce j�zyki Xpdf zawieraj� pliki CMap, kodowania oraz
r�ne inne informacje konfiguracyjne niezb�dne b�d� przydatne przy
okre�lonych zestawach znak�w. (Nie zawieraj� �adnych font�w).
Ten pakiet zawiera pliki potrzebne do u�ywania narz�dzi Xpdf z
japo�skimi plikami PDF.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xpdf/CMap-japanese

install *.unicodeMap $RPM_BUILD_ROOT%{_datadir}/xpdf
install *.cidToUnicode $RPM_BUILD_ROOT%{_datadir}/xpdf
install CMap/* $RPM_BUILD_ROOT%{_datadir}/xpdf/CMap-japanese

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/xpdfrc ]; then
	echo 'unicodeMap	ISO-2022-JP	/usr/share/xpdf/ISO-2022-JP.unicodeMap' >> /etc/xpdfrc
	echo 'unicodeMap	EUC-JP		/usr/share/xpdf/EUC-JP.unicodeMap' >> /etc/xpdfrc
	echo 'unicodeMap	Shift-JIS	/usr/share/xpdf/Shift-JIS.unicodeMap' >> /etc/xpdfrc
	echo 'cidToUnicode	Adobe-Japan1	/usr/share/xpdf/Adobe-Japan1.cidToUnicode' >> /etc/xpdfrc
	echo 'cMapDir		Adobe-Japan1	/usr/share/xpdf/CMap-japanese' >> /etc/xpdfrc
	echo 'toUnicodeDir			/usr/share/xpdf/CMap-japanese' >> /etc/xpdfrc
	echo 'displayCIDFontX	Adobe-Japan1	"-*-fixed-medium-r-normal-*-%s-*-*-*-*-*-jisx0208.1983-0" ISO-2022-JP' >> /etc/xpdfrc
else
 if ! grep -q 'ISO-2022-JP\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	ISO-2022-JP	/usr/share/xpdf/ISO-2022-JP.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q 'EUC-JP\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	EUC-JP		/usr/share/xpdf/EUC-JP.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q 'Shift-JIS\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	Shift-JIS	/usr/share/xpdf/Shift-JIS.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q 'Adobe-Japan1\.cidToUnicode' /etc/xpdfrc; then
	echo 'cidToUnicode	Adobe-Japan1	/usr/share/xpdf/Adobe-Japan1.cidToUnicode' >> /etc/xpdfrc
 fi
 if ! grep -q 'CMap-japanese' /etc/xpdfrc; then
	echo 'cMapDir		Adobe-Japan1	/usr/share/xpdf/CMap-japanese' >> /etc/xpdfrc
	echo 'toUnicodeDir			/usr/share/xpdf/CMap-japanese' >> /etc/xpdfrc
 fi
 if ! grep -q -e '-\*-fixed-medium-r-normal-\*-%s-\*-\*-\*-\*-\*-jisx0208\.1983-0' /etc/xpdfrc; then
	echo 'displayCIDFontX	Adobe-Japan1	"-*-fixed-medium-r-normal-*-%s-*-*-*-*-*-jisx0208.1983-0" ISO-2022-JP' >> /etc/xpdfrc
 fi
fi

%preun
umask 022
grep -v 'ISO-2022-JP\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
grep -v 'EUC-JP\.unicodeMap' /etc/xpdfrc.new > /etc/xpdfrc
grep -v 'Shift-JIS\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
grep -v 'Adobe-Japan1\.cidToUnicode' /etc/xpdfrc.new > /etc/xpdfrc
grep -v 'CMap-japanese' /etc/xpdfrc > /etc/xpdfrc.new
grep -v -e '-\*-fixed-medium-r-normal-\*-%s-\*-\*-\*-\*-\*-jisx0208\.1983-0' /etc/xpdfrc.new > /etc/xpdfrc
rm -f /etc/xpdfrc.new

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/*
