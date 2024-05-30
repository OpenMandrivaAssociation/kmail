%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%global optflags %{optflags} -fexceptions

Summary:	KDE email client
Name:		kmail
Version:	23.08.5
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# https://cgit.kde.org/kmail.git/patch/?id=97e165dcf5a851ee10526631d24f9af7736da2e6
Patch0:		kmail-dont-crash-on-logout.patch
BuildRequires:	cmake(ECM)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(ldap)
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	cmake(Qt5Keychain)
BuildRequires:	cmake(KPim5WebEngineViewer)
BuildRequires:	cmake(KPim5AkonadiSearch)
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
BuildRequires:	cmake(KF5IconThemes)
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
BuildRequires:	cmake(KPim5Akonadi)
BuildRequires:	cmake(KPim5AkonadiContact)
BuildRequires:	cmake(KPim5AkonadiMime)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KPim5CalendarUtils)
BuildRequires:	cmake(KPim5IdentityManagement)
BuildRequires:	cmake(KPim5Ldap)
BuildRequires:	cmake(KPim5MailTransport)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KPim5KontactInterface)
BuildRequires:	cmake(KPim5Mime)
BuildRequires:	cmake(KPim5Gravatar)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KPim5LibKSieve)
BuildRequires:	cmake(KPim5MailCommon)
BuildRequires:	cmake(KPim5MessageCore)
BuildRequires:	cmake(KPim5MessageComposer)
BuildRequires:	cmake(KPim5MessageList)
BuildRequires:	cmake(KPim5MessageViewer)
BuildRequires:	cmake(KPim5PimCommonAkonadi)
BuildRequires:	cmake(KPim5TemplateParser)
BuildRequires:	cmake(KPim5Tnef)
BuildRequires:	cmake(MailTransportDBusService)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(KUserFeedback)
Requires:	kdepim-runtime
Suggests:	kdepim-addons
Suggests:	pinentry-qt5
Suggests:	ksshaskpass
Requires:	sasl-plug-plain
Requires:	sasl-plug-ntlm
Requires:	sasl-plug-login
Requires:	sasl-plug-digestmd5
Requires:	akonadi-archivemail-agent
Requires:	akonadi-followupreminder-agent
Requires:	akonadi-import-wizard
Requires:	akonadi-mailfilter-agent
Requires:	akonadi-sendlater-agent
Requires:	akonadi-unifiedmailbox-agent
Requires:	grantlee
Requires:	grantlee-editor
Requires:	ktnef
Requires:	mbox-importer
Requires:	pim-data-exporter
Requires:	pim-sieve-editor
Obsoletes:	kdepim < 3:17.04.0
Provides:	kmail2 = %{EVRD}
Obsoletes:	messageviewer
Conflicts:	kontact < 3:17.04.0
Conflicts:	kaddressbook < 3:17.04.0
Conflicts:	knotes < 3:17.04.0
Conflicts:	korganizer < 3:17.04.0

%description
KMail is the email component of Kontact, the integrated personal
information manager of KDE.

%files -f %{name}.lang -f kmail-refresh-settings.lang
%{_bindir}/akonadi_mailmerge_agent
%{_datadir}/akonadi/agents/mailmergeagent.desktop
%{_datadir}/knotifications5/akonadi_mailmerge_agent.notifyrc
%{_kde5_applicationsdir}/kmail_view.desktop
%{_kde5_applicationsdir}/org.kde.kmail2.desktop
%{_datadir}/applications/org.kde.kmail-refresh-settings.desktop
%{_bindir}/kmail
%{_bindir}/kmail-refresh-settings
%{_datadir}/config.kcfg/kmail.kcfg
%dir %{_datadir}/kmail2
%{_datadir}/kmail2/*
%{_docdir}/*/*/kmail2
%{_iconsdir}/*/*/emblems/*.svg
%{_iconsdir}/*/*/apps/kmail.*
%{_datadir}/knotifications5/kmail2.notifyrc
%{_datadir}/qlogging-categories5/kmail.categories
%{_datadir}/qlogging-categories5/kmail.renamecategories
%{_kde5_xmlguidir}/kontactsummary/kontactsummary_part.rc
%{_datadir}/metainfo/org.kde.kmail2.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmail.*.xml
%{_datadir}/dbus-1/services/org.kde.kmail.service
%{_qt5_plugindir}/kmailpart.so
%{_qt5_plugindir}/pim5/kontact/kontact_kmailplugin.so
%{_qt5_plugindir}/pim5/kontact/kontact_summaryplugin.so
%{_qt5_plugindir}/pim5/kcms/kmail/kcm_kmail_accounts.so
%{_qt5_plugindir}/pim5/kcms/kmail/kcm_kmail_appearance.so
%{_qt5_plugindir}/pim5/kcms/kmail/kcm_kmail_composer.so
%{_qt5_plugindir}/pim5/kcms/kmail/kcm_kmail_misc.so
%{_qt5_plugindir}/pim5/kcms/kmail/kcm_kmail_plugins.so
%{_qt5_plugindir}/pim5/kcms/kmail/kcm_kmail_security.so
%{_qt5_plugindir}/pim5/kcms/summary/kcmkmailsummary.so
%{_qt5_plugindir}/pim5/kcms/summary/kcmkontactsummary.so

#-----------------------------------------------------------------------------

%package -n akonadi-archivemail-agent
Summary:	Akonadi archivemail agent
Group:		Graphical desktop/KDE

%description -n akonadi-archivemail-agent
Akonadi archivemail agent.

%files -n akonadi-archivemail-agent -f akonadi_archivemail_agent.lang
%{_bindir}/akonadi_archivemail_agent
%{_datadir}/akonadi/agents/archivemailagent.desktop
%{_datadir}/config.kcfg/archivemailagentsettings.kcfg
%{_docdir}/*/*/akonadi_archivemail_agent
%{_datadir}/knotifications5/akonadi_archivemail_agent.notifyrc
%{_qt5_plugindir}/pim5/akonadi/config/archivemailagentconfig.so

#-----------------------------------------------------------------------------

%package -n akonadi-followupreminder-agent
Summary:	Akonadi followupreminder agent
Group:		Graphical desktop/KDE

%description -n akonadi-followupreminder-agent
Akonadi followup reminder agent allows to remind you when an email was not
answered.

%files -n akonadi-followupreminder-agent -f akonadi_followupreminder_agent.lang
%{_bindir}/akonadi_followupreminder_agent
%{_datadir}/akonadi/agents/followupreminder.desktop
%{_docdir}/*/*/akonadi_followupreminder_agent
%{_datadir}/knotifications5/akonadi_followupreminder_agent.notifyrc
%{_qt5_plugindir}/pim5/akonadi/config/followupreminderagentconfig.so

#-----------------------------------------------------------------------------

%package -n akonadi-mailfilter-agent
Summary:	Akonadi mailfilter agent
Group:		Graphical desktop/KDE

%description -n akonadi-mailfilter-agent
Akonadi mailfilter agent.

%files -n akonadi-mailfilter-agent -f akonadi_mailfilter_agent.lang -f akonadi_mailmerge_agent.lang
%{_bindir}/akonadi_mailfilter_agent
%{_datadir}/akonadi/agents/mailfilteragent.desktop
%{_datadir}/knotifications5/akonadi_mailfilter_agent.notifyrc

#-----------------------------------------------------------------------------

%package -n akonadi-sendlater-agent
Summary:	Akonadi sendlater agent
Group:		Graphical desktop/KDE

%description -n akonadi-sendlater-agent
Akonadi sendlater agent.

%files -n akonadi-sendlater-agent -f akonadi_sendlater_agent.lang
%{_bindir}/akonadi_sendlater_agent
%{_datadir}/akonadi/agents/sendlateragent.desktop
%{_docdir}/*/*/akonadi_sendlater_agent
%{_datadir}/knotifications5/akonadi_sendlater_agent.notifyrc

#-----------------------------------------------------------------------------

%package -n akonadi-unifiedmailbox-agent
Summary:	Akonadi unified mailbox agent
Group:		Graphical desktop/KDE

%description -n akonadi-unifiedmailbox-agent
Akonadi unified mailbox agent.

%files -n akonadi-unifiedmailbox-agent -f akonadi_unifiedmailbox_agent.lang
%{_bindir}/akonadi_unifiedmailbox_agent
%{_datadir}/akonadi/agents/unifiedmailboxagent.desktop

#----------------------------------------------------------------------------

%package -n ktnef
Summary:	KDE TNEF file viewer
Group:		Graphical desktop/KDE

%description -n ktnef
The TNEF file viewer allows you to handle mail attachments using the TNEF
format. These attachments are usually found in mails coming from Microsoft
mail servers and embed the mail properties as well as the actual attachments.

%files -n ktnef -f ktnef.lang
%{_kde5_applicationsdir}/org.kde.ktnef.desktop
%{_bindir}/ktnef
%{_docdir}/*/*/ktnef
%{_iconsdir}/*/*/actions/ktnef_extract_*.*
%{_iconsdir}/*/*/apps/ktnef.*

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


%find_lang akonadi_archivemail_agent
%find_lang akonadi_followupreminder_agent
%find_lang akonadi_mailfilter_agent
%find_lang akonadi_mailmerge_agent
%find_lang akonadi_sendlater_agent
%find_lang akonadi_unifiedmailbox_agent
%find_lang %{name}
%find_lang %{name}-refresh-settings
%find_lang ktnef
