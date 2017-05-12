Summary:	KDE email client
Name:		kmail
Version:	17.04.0
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	boost-devel
BuildRequires:	openldap-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	cmake(KF5WebEngineViewer)
BuildRequires:	cmake(KF5AkonadiSearch)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5Ldap)
BuildRequires:	cmake(KF5MailTransportAkonadi)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5KontactInterface)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5FollowupReminder)
BuildRequires:	cmake(KF5Gravatar)
BuildRequires:	cmake(KF5KdepimDBusInterfaces)
BuildRequires:	cmake(KF5LibkdepimAkonadi)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5LibKSieve)
BuildRequires:	cmake(KF5MailCommon)
BuildRequires:	cmake(KF5MessageCore)
BuildRequires:	cmake(KF5MessageComposer)
BuildRequires:	cmake(KF5MessageList)
BuildRequires:	cmake(KF5MessageViewer)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(KF5SendLater)
BuildRequires:	cmake(KF5TemplateParser)
BuildRequires:	cmake(KF5Tnef)
BuildRequires:	cmake(MailTransportDBusService)
Requires:	kdepim-runtime
Suggests:	kdepim-addons
Requires:	akonadi-archivemail-agent
Requires:	akonadi-followupreminder-agent
Requires:	akonadi-import-wizard
Requires:	akonadi-mailfilter-agent
Requires:	akonadi-sendlater-agent
Requires:	grantlee-editor
Requires:	ktnef
Requires:	mbox-importer
Requires:	pim-data-exporter
Requires:	pim-sieve-editor
Requires:	pim-storage-service-manager
Obsoletes:	kdepim < 3:17.04

%description
KMail is the email component of Kontact, the integrated personal
information manager of KDE.

%files
%{_kde5_applicationsdir}/kmail_view.desktop
%{_kde5_applicationsdir}/org.kde.kmail.desktop
%{_bindir}/kmail
%{_datadir}/config.kcfg/kmail.kcfg
%{_datadir}/kconf_update/kmail*
%dir %{_datadir}/kmail2
%{_datadir}/kmail2/*
%{_datadir}/kontact/ksettingsdialog/kmail.setdlg
%{_datadir}/kontact/ksettingsdialog/summary.setdlg
%{_datadir}/messageviewer/about/default/introduction_kmail.html
%{_docdir}/*/*/kmail
%{_iconsdir}/hicolor/*/apps/kmail.*
%{_kde5_notificationsdir}/kmail2.notifyrc
%{_kde5_services}/kcm_kpimidentities.desktop
%{_kde5_services}/kcmkmailsummary.desktop
%{_kde5_services}/kcmkontactsummary.desktop
%{_kde5_services}/kmail_*.desktop
%{_kde5_services}/kontact/kmailplugin.desktop
%{_kde5_services}/kontact/summaryplugin.desktop
%{_kde5_services}/ServiceMenus/kmail_addattachmentservicemenu.desktop
%{_kde5_servicetypes}/dbusmail.desktop
%{_kde5_sysconfdir}/xdg/kmail.categories
%{_kde5_sysconfdir}/xdg/kmail.renamecategories
%{_kde5_xmlguidir}/kmail2/*.rc
%{_kde5_xmlguidir}/kontactsummary/kontactsummary_part.rc
%{_datadir}/metainfo/org.kde.kmail.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmail.*.xml
%{_qt5_plugindir}/kcm_kmail.so
%{_qt5_plugindir}/kcm_kmailsummary.so
%{_qt5_plugindir}/kcm_kontactsummary.so
%{_qt5_plugindir}/kcm_kpimidentities.so
%{_qt5_plugindir}/kmailpart.so
%{_qt5_plugindir}/kontact_kmailplugin.so
%{_qt5_plugindir}/kontact_summaryplugin.so

#-----------------------------------------------------------------------------

%package -n akonadi-archivemail-agent
Summary:	Akonadi archivemail agent
Group:		Graphical desktop/KDE

%description -n akonadi-archivemail-agent
Akonadi archivemail agent.

%files -n akonadi-archivemail-agent
%{_bindir}/akonadi_archivemail_agent
%{_datadir}/akonadi/agents/archivemailagent.desktop
%{_datadir}/config.kcfg/archivemailagentsettings.kcfg
%{_docdir}/*/*/akonadi_archivemail_agent
%{_kde5_notificationsdir}/akonadi_archivemail_agent.notifyrc

#-----------------------------------------------------------------------------

%package -n akonadi-followupreminder-agent
Summary:	Akonadi followupreminder agent
Group:		Graphical desktop/KDE

%description -n akonadi-followupreminder-agent
Akonadi followup reminder agent allows to remind you when an email was not
answered.

%files -n akonadi-followupreminder-agent
%{_bindir}/akonadi_followupreminder_agent
%{_datadir}/akonadi/agents/followupreminder.desktop
%{_docdir}/*/*/akonadi_followupreminder_agent
%{_kde5_notificationsdir}/akonadi_followupreminder_agent.notifyrc

#-----------------------------------------------------------------------------

%package -n akonadi-mailfilter-agent
Summary:	Akonadi mailfilter agent
Group:		Graphical desktop/KDE

%description -n akonadi-mailfilter-agent
Akonadi mailfilter agent.

%files -n akonadi-mailfilter-agent
%{_bindir}/akonadi_mailfilter_agent
%{_datadir}/akonadi/agents/mailfilteragent.desktop
%{_kde5_notificationsdir}/akonadi_mailfilter_agent.notifyrc

#-----------------------------------------------------------------------------

%package -n akonadi-sendlater-agent
Summary:	Akonadi sendlater agent
Group:		Graphical desktop/KDE

%description -n akonadi-sendlater-agent
Akonadi sendlater agent.

%files -n akonadi-sendlater-agent
%{_bindir}/akonadi_sendlater_agent
%{_datadir}/akonadi/agents/sendlateragent.desktop
%{_docdir}/*/*/akonadi_sendlater_agent
%{_kde5_notificationsdir}/akonadi_sendlater_agent.notifyrc

#----------------------------------------------------------------------------

%package -n ktnef
Summary:	KDE TNEF file viewer
Group:		Graphical desktop/KDE

%description -n ktnef
The TNEF file viewer allows you to handle mail attachments using the TNEF
format. These attachments are usually found in mails coming from Microsoft
mail servers and embed the mail properties as well as the actual attachments.

%files -n ktnef
%{_kde5_applicationsdir}/org.kde.ktnef.desktop
%{_bindir}/ktnef
%{_docdir}/*/*/ktnef
%{_iconsdir}/*/*/actions/ktnef_extract_*.*
%{_iconsdir}/*/*/apps/ktnef.*
%{_sysconfdir}/xdg/ktnef.categories

#----------------------------------------------------------------------------

%define kmailprivate_major 5
%define libkmailprivate %mklibname kmailprivate %{kmailprivate_major}

%package -n %{libkmailprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libkmailprivate}
KDE PIM shared library.

%files -n %{libkmailprivate}
%{_kde5_libdir}/libkmailprivate.so.%{kmailprivate_major}*

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
