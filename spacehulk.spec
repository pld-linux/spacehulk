Summary:	Board game which takes place in the world of Warhammer 40000
Summary(pl):	Gra planszowa tocz±ca siê w ¶wiecie Warhammer'a 40000
Name:		spacehulk
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://savannah.nongnu.org/download/spacehulk/main.pkg/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Icon:		spacehulk.xpm
URL:		http://savannah.nongnu.org/projects/spacehulk/
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Space Hulk is a great board game which takes place in the world of
Warhammer 40000. It is a two player turn-based game where one player
plays the 'Marine', the other player plays the alien called
'Genestealer'. This video game is a complete conversion of the board
game with the 2nd edition rules. It features playing over the network,
either in real time or asynchronously via email.

%description -l pl
Space Hulk jest gr± planszow±, której akcja toczy siê w ¶wiecie
Warhammera 40000. Jest to turowa gra dla dwóch osób. Jeden gracz
odgrywa 'Marine', a drugi wciela sie w obcego zwanego 'Genokrad'. Jest
to kompletna konwersja gry planszowej z zasadami 2-giej edycji.
Rozgrywka moze toczyæ siê przez sieæ, w czasie rzeczywistym, lub
asynchronicznie poprzez e-mail.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Board,%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Board
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/spacehulk
%{_applnkdir}/Games/Board/spacehulk.desktop
%{_pixmapsdir}/spacehulk.png
