# TODO:
# - disable using guichan files included with package

Summary:	Simple solar system build-and-conquer game
Summary(pl.UTF-8):	Prosta gra typu "buduj i zdobywaj"
Name:		qonk
Version:	0.3.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/qonk/%{name}-%{version}.tar.gz
# Source0-md5:	9491980477ac5beb5bba6b8234d2ddfd
Patch0:		%{name}-headers.patch
Patch1:		%{name}-malloc.patch
URL:		http://scratchpad.wikia.com/wiki/Qonk
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_gfx-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qonk is a small build-and-conquer strategy game with very simple
rules. The setting of the game is a solar system of planets. Your goal
is to conquer all of the planets in the game by sending ships there.
Planets that are under your control generate new ships. Simple AI
players are playing against you. As you gain more experience
throughout the game, more AI players in bigger systems have to be
kicked out.

%description -l pl.UTF-8
Qonk jest mała grą strategiczną typu "buduj i zdobywaj" z bardzo
prostymi zasadami. Gra umiejscowiona jest w układzie słonecznym
planet. Celem gracza jest podbicie wszystkich planet przez wysyłanie
tam statków. Planety, które znajdują się pod kontrolą gracza,
wytwarzają nowe statki. Zagrożeniem są prości przeciwnicy sterowani
przez komputer. Im więcej doświadczenia zdobędzie gracz, tym więcej
przeciwników będzie musiał pokonać w coraz większych układach.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README THANKYOU TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
