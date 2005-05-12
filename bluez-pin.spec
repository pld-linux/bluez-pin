Summary:	Bluetooth PIN manager
Summary(pl):	Zarz±dca kodów PIN dla Bluetooth
Name:		bluez-pin
Version:	0.25
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://gpe.handhelds.org/projects/gpe/source/%{name}-%{version}.tar.gz
# Source0-md5:	6f3c368ddef1d6cb8dced822bc5242b2
URL:		http://gpe.handhelds.org/projects/bluez-pin.shtml
BuildRequires:	GConf2-devel >= 2.0.0
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-glib-devel
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

%description -l pl
Bardzo prosty program pilnuj±cy numerów PIN u¿ywanych do parowania
urz±dzeñ Bluetooth. Kiedy wymagany jest PIN dla przychodz±cego lub
wychodz±cego po³±czenia, pokazuje okienko umo¿liwiaj±ce wprowadzenie
kodu. PIN-y opcjonalnie mog± byæ przechowywane w bazie danych do
u¿ywania z prymitywnymi urz±dzeniami nie potrafi±cymi zapamiêtaæ
informacji o parowaniu miêdzy sesjami.

%prep
%setup -q

sed -i -e 's/-O2 -g/%{rpmcflags}/' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	SYSCONFDIR=%{_sysconfdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/bluez-pin
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dbus-1/system.d/bluez.conf
%{_pixmapsdir}/bt-logo.png
%{_datadir}/%{name}
