Summary:	Board game which takes place in the world of Warhammer 40000
Summary(pl.UTF-8):	Gra planszowa tocząca się w świecie Warhammer'a 40000
Name:		spacehulk
Version:	1.4.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://savannah.nongnu.org/download/spacehulk/main.pkg/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7bdc457d76be495df9ae28038acaaeca
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://savannah.nongnu.org/projects/spacehulk/
BuildRequires:	qt-devel >= 3:3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Space Hulk is a great board game which takes place in the world of
Warhammer 40000. It is a two player turn-based game where one player
plays the 'Marine', the other player plays the alien called
'Genestealer'. This video game is a complete conversion of the board
game with the 2nd edition rules. It features playing over the network,
either in real time or asynchronously via email.

%description -l pl.UTF-8
Space Hulk jest grą planszową, której akcja toczy się w świecie
Warhammera 40000. Jest to turowa gra dla dwóch osób. Jeden gracz
odgrywa 'Marine', a drugi wciela się w obcego zwanego 'Genokrad'. Jest
to kompletna konwersja gry planszowej z zasadami 2-giej edycji.
Rozgrywka może toczyć się przez sieć, w czasie rzeczywistym, lub
asynchronicznie poprzez e-mail.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/spacehulk
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/spacehulk.png
