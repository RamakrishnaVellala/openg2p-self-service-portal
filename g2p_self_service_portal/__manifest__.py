{
    "name": "G2P Self Service Portal",
    "category": "G2P",
    "version": "15.0.1.1.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://github.com/OpenG2P/openg2p-self-service-portal",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": [
        "g2p_registry_base",
        "g2p_registry_individual",
        "g2p_programs",
        "website",
        "web"
          ],
    "data": [
        "views/g2p_self_service_base.xml",
        "views/g2p_self_service_login.xml",
        "views/g2p_self_service_dashboard.xml",
        "views/g2p_self_service_allprograms.xml",
        "views/g2p_self_service_myprofile.xml",
        "views/g2p_self_service_aboutus.xml",
        "views/g2p_self_service_contactus.xml",
        "views/g2p_self_service_otherpage.xml",
        "views/g2p_self_service_help.xml",
        "views/auth_oauth_provider.xml",
        "views/g2p_self_service_form_page_template.xml",
        "views/g2p_self_service_program_view.xml",
        "views/g2p_self_service_default_form.xml",
        "views/g2p_self_service_submitted_forms.xml",  
        "views/res_config_settings.xml",

    ],
    "assets": {
        "web.assets_backend": [],
        "web.assets_qweb": [
            #   "views/g2p_self_service_portal.doughnut_chart.xml",
        ],
        "web.assets_frontend": [
            "g2p_self_service_portal/static/src/js/self_service_form_action.js",
            # # "g2p_self_service_portal/static/src/js/self_service_pie_chart.js",
            # "g2p_self_service_portal/static/src/js/self-service_search_sort.js",
            # "g2p_self_service_portal/static/src/js/self-service_search_sort_all.js",
            # "g2p_self_service_portal/static/src/js/self_service_welcome_alert.js"
            
        ],
        "web.assets_common": [
            # "g2p_self_service_portal/static/src/css/base.css",
        ],
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
