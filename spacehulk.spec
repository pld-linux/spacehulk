Summary:	Board game which takes place in the world of Warhammer 40000.
Summary(pl):	Gra planszowa toczaca sie w swiecie Warhammer'a 40000.
Name:		spacehulk
Version:	1.2
Release:	1
License:	GPL
Group:		Games/Entertainment
Source0:	http://savannah.nongnu.org/download/spacehulk/spacehulk-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://savannah.nongnu.org/projects/spacehulk/
BuildRequires:  (qt >= 3.1.0)
Requires:       qt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Space Hulk is a great board game which takes place in the world of Warhammer 40000. It is a two player turn-based game where one player plays the 'Marine', the other player plays the alien called 'Genestealer'. This video game is a complete conversion of the board game with the 2nd edition rules. It features playing over the network, either in real time or asynchronously via email.

%description -l pl
Space Hulk jest gra planszowa, ktorej akcja toczy sie w swiecie
Warhammera 40000. Jest to turowa gra dla dwoch osob, jeden gracz odgrywa 
'Marine', a drugi wciela sie w obcego zwanego 'Genokrad'. Jest to kompletna
konwersja gry planszowej z zasadami 2giej edycji. Rozgrywka moze toczyc sie 
przez siec, w czasie rzeczywistym, lub asynchronicznie poprzez email.

%prep
%setup -q -n %{name}-%{version}

%build
./configure \
	--prefix=/usr/X11R6 \
	--bindir=/usr/X11R6/bin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/X11R6/share/spacehulk,/usr/X11R6/bin,/usr/X11R6/share/applnk/Games/Board,%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Board
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %dir /usr/X11R6/bin/*
%dir /usr/X11R6/share/spacehulk/levels/*
%dir /usr/X11R6/share/spacehulk/*
%dir /usr/X11R6/share/spacehulk/sounds/*
%dir /usr/X11R6/share/spacehulk/themes/BrownSimple/*
%dir /usr/X11R6/share/spacehulk/themes/Deathwing/*
%doc AUTHORS COPYING NEWS README TODO
%{_applnkdir}/Games/Board/spacehulk.desktop
%{_pixmapsdir}/spacehulk.xpm
