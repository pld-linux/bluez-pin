Summary:	Bluetooth PIN manager
Summary(pl.UTF-8):	Zarządca kodów PIN dla Bluetooth
Name:		bluez-pin
Version:	0.30
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.handhelds.org/projects/gpe/source/%{name}-%{version}.tar.bz2
# Source0-md5:	518226e84ea0925511184fe85f89e901
URL:		http://gpe.handhelds.org/projects/bluez-pin.shtml
BuildRequires:	GConf2-devel >= 2.0.0
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-glib-devel >= 0.50
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple program which takes care of the PIN numbers used
to pair Bluetooth devices. When a PIN is required for either an
incoming or outgoing connection, it pops up a window to allow the code
to be entered. PINs can optionally be saved in a persistent database,
for use with dumb devices that are unable to remember pairing
information across sessions.

%description -l pl.UTF-8
Bardzo prosty program pilnujący numerów PIN używanych do parowania
urządzeń Bluetooth. Kiedy wymagany jest PIN dla przychodzącego lub
wychodzącego połączenia, pokazuje okienko umożliwiające wprowadzenie
kodu. PIN-y opcjonalnie mogą być przechowywane w bazie danych do
używania z prymitywnymi urządzeniami nie potrafiącymi zapamiętać
informacji o parowaniu między sesjami.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
#-f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/bluez-pin
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/bluez.conf
%{_pixmapsdir}/bt-logo.png
%{_datadir}/%{name}
