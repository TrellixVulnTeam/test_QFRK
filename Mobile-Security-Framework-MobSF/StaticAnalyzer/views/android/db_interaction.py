# -*- coding: utf_8 -*-
import logging

from django.conf import settings
from django.db.models import QuerySet

from MobSF.utils import python_dict, python_list

from StaticAnalyzer.models import StaticAnalyzerAndroid
from StaticAnalyzer.models import RecentScansDB

"""Module holding the functions for the db."""


logger = logging.getLogger(__name__)


def get_context_from_db_entry(db_entry: QuerySet) -> dict:
    """Return the context for APK/ZIP from DB."""
    try:
        logger.info('Analysis is already Done. Fetching data from the DB...')
        context = {
            'version': settings.MOBSF_VER,
            'title': 'Static Analysis',
            'file_name': db_entry[0].FILE_NAME,
            'app_name': db_entry[0].APP_NAME,
            'app_type': db_entry[0].APP_TYPE,
            'size': db_entry[0].SIZE,
            'md5': db_entry[0].MD5,
            'sha1': db_entry[0].SHA1,
            'sha256': db_entry[0].SHA256,
            'package_name': db_entry[0].PACKAGE_NAME,
            'main_activity': db_entry[0].MAIN_ACTIVITY,
            # 'exported_activities': db_entry[0].EXPORTED_ACTIVITIES,
            # 'browsable_activities': python_dict(
            #     db_entry[0].BROWSABLE_ACTIVITIES),
            # 'activities': python_list(db_entry[0].ACTIVITIES),
            # 'receivers': python_list(db_entry[0].RECEIVERS),
            # 'providers': python_list(db_entry[0].PROVIDERS),
            # 'services': python_list(db_entry[0].SERVICES),
            # 'libraries': python_list(db_entry[0].LIBRARIES),
            'target_sdk': db_entry[0].TARGET_SDK,
            'max_sdk': db_entry[0].MAX_SDK,
            'min_sdk': db_entry[0].MIN_SDK,
            'version_name': db_entry[0].VERSION_NAME,
            'version_code': db_entry[0].VERSION_CODE,
            'icon_hidden': db_entry[0].ICON_HIDDEN,
            'icon_found': db_entry[0].ICON_FOUND,
            # 'permissions': python_dict(db_entry[0].PERMISSIONS),
            # 'certificate_analysis': python_dict(
            #     db_entry[0].CERTIFICATE_ANALYSIS),
            'manifest_analysis': python_list(db_entry[0].MANIFEST_ANALYSIS),
            'network_security': python_list(db_entry[0].NETWORK_SECURITY),
            # 'binary_analysis': python_list(db_entry[0].BINARY_ANALYSIS),
            # 'file_analysis': python_list(db_entry[0].FILE_ANALYSIS),
            # 'android_api': python_dict(db_entry[0].ANDROID_API),
            'code_analysis': python_dict(db_entry[0].CODE_ANALYSIS),
            # insert
            'debug_analysis': python_dict(db_entry[0].DEBUG_ANALYSIS),
            'root_analysis': python_dict(db_entry[0].ROOT_ANALYSIS),
            'webview_analysis': python_dict(db_entry[0].WEBVIEW_ANALYSIS),
            'apkid': python_dict(db_entry[0].APKID),
            # end
            # 'niap_analysis': python_dict(db_entry[0].NIAP_ANALYSIS),
            # 'urls': python_list(db_entry[0].URLS),
            # 'domains': python_dict(db_entry[0].DOMAINS),
            # 'emails': python_list(db_entry[0].EMAILS),
            # 'strings': python_list(db_entry[0].STRINGS),
            # 'firebase_urls': python_list(db_entry[0].FIREBASE_URLS),
            # 'files': python_list(db_entry[0].FILES),
            # 'exported_count': python_dict(db_entry[0].EXPORTED_COUNT),
            # 'apkid': python_dict(db_entry[0].APKID),
            # 'trackers': python_dict(db_entry[0].TRACKERS),
            # 'playstore_details': python_dict(db_entry[0].PLAYSTORE_DETAILS),
            # 'secrets': python_list(db_entry[0].SECRETS),
        }
        return context
    except Exception:
        logger.exception('Fetching from DB')


# def get_context_from_analysis(app_dic,
#                               man_data_dic,
#                               man_an_dic,
#                               code_an_dic,
#                               cert_dic,
#                               bin_anal,
#                               apk_id,
#                               trackers) -> dict:
def get_context_from_analysis(app_dic,
                              man_data_dic,
                              man_an_dic,
                              code_an_dic,
                              debug_an_dic,
                              root_an_dic,
                              webview_an_dic,
                              apk_id,
                              ) -> dict:
    """Get the context for APK/ZIP from analysis results."""
    try:
        context = {
            'title': 'Static Analysis',
            'version': settings.MOBSF_VER,
            'file_name': app_dic['app_name'],
            'app_name': app_dic['real_name'],
            'app_type': app_dic['zipped'],
            'size': app_dic['size'],
            'md5': app_dic['md5'],
            'sha1': app_dic['sha1'],
            'sha256': app_dic['sha256'],
            'package_name': man_data_dic['packagename'],
            'main_activity': man_data_dic['mainactivity'],
            # 'exported_activities': man_an_dic['exported_act'],
            # 'browsable_activities': man_an_dic['browsable_activities'],
            # 'activities': man_data_dic['activities'],
            # 'receivers': man_data_dic['receivers'],
            # 'providers': man_data_dic['providers'],
            # 'services': man_data_dic['services'],
            # 'libraries': man_data_dic['libraries'],
            'target_sdk': man_data_dic['target_sdk'],
            'max_sdk': man_data_dic['max_sdk'],
            'min_sdk': man_data_dic['min_sdk'],
            'version_name': man_data_dic['androvername'],
            'version_code': man_data_dic['androver'],
            'icon_hidden': app_dic['icon_hidden'],
            'icon_found': app_dic['icon_found'],
            # 'certificate_analysis': cert_dic,
            # 'permissions': man_an_dic['permissons'],
            'manifest_analysis': man_an_dic['manifest_anal'],
            'network_security': man_an_dic['network_security'],
            # 'binary_analysis': bin_anal,
            # 'file_analysis': app_dic['certz'],
            # 'android_api': code_an_dic['api'],
            'code_analysis': code_an_dic['findings'],
            # insert
            'debug_analysis': debug_an_dic['findings'],
            'root_analysis': root_an_dic['findings'],
            'webview_an_dic': webview_an_dic['findings'],
            'apkid': apk_id,
            # end
            # 'niap_analysis': code_an_dic['niap'],
            # 'urls': code_an_dic['urls'],
            # 'domains': code_an_dic['domains'],
            # 'emails': code_an_dic['emails'],
            # 'strings': app_dic['strings'],
            # 'firebase_urls': code_an_dic['firebase'],
            # 'files': app_dic['files'],
            # 'exported_count': man_an_dic['exported_cnt'],
            # 'apkid': apk_id,
            # 'trackers': trackers,
            # 'playstore_details': app_dic['playstore'],
            # 'secrets': app_dic['secrets'],
        }
        return context
    except Exception:
        logger.exception('Rendering to Template')


# def save_or_update(update_type,
#                    app_dic,
#                    man_data_dic,
#                    man_an_dic,
#                    code_an_dic,
#                    cert_dic,
#                    bin_anal,
#                    apk_id,
#                    trackers) -> None:
def save_or_update(update_type,
                   app_dic,
                   man_data_dic,
                   man_an_dic,
                   code_an_dic,
                   debug_an_dic,
                   root_an_dic,
                   webview_an_dic,
                   apk_id,
                   ) -> None:
    """Save/Update an APK/ZIP DB entry."""
    try:
        values = {
            'FILE_NAME': app_dic['app_name'],
            'APP_NAME': app_dic['real_name'],
            'APP_TYPE': app_dic['zipped'],
            'SIZE': app_dic['size'],
            'MD5': app_dic['md5'],
            'SHA1': app_dic['sha1'],
            'SHA256': app_dic['sha256'],
            'PACKAGE_NAME': man_data_dic['packagename'],
            'MAIN_ACTIVITY': man_data_dic['mainactivity'],
            # 'EXPORTED_ACTIVITIES': man_an_dic['exported_act'],
            # 'BROWSABLE_ACTIVITIES': man_an_dic['browsable_activities'],
            # 'ACTIVITIES': man_data_dic['activities'],
            # 'RECEIVERS': man_data_dic['receivers'],
            # 'PROVIDERS': man_data_dic['providers'],
            # 'SERVICES': man_data_dic['services'],
            # 'LIBRARIES': man_data_dic['libraries'],
            'TARGET_SDK': man_data_dic['target_sdk'],
            'MAX_SDK': man_data_dic['max_sdk'],
            'MIN_SDK': man_data_dic['min_sdk'],
            'VERSION_NAME': man_data_dic['androvername'],
            'VERSION_CODE': man_data_dic['androver'],
            'ICON_HIDDEN': app_dic['icon_hidden'],
            'ICON_FOUND': app_dic['icon_found'],
            # 'CERTIFICATE_ANALYSIS': cert_dic,
            # 'PERMISSIONS': man_an_dic['permissons'],
            'MANIFEST_ANALYSIS': man_an_dic['manifest_anal'],
            # 'BINARY_ANALYSIS': bin_anal,
            # 'FILE_ANALYSIS': app_dic['certz'],
            # 'ANDROID_API': code_an_dic['api'],
            'CODE_ANALYSIS': code_an_dic['findings'],
            # insert
            'DEBUG_ANALYSIS': debug_an_dic['findings'],
            'ROOT_ANALYSIS': root_an_dic['findings'],
            'WEBVIEW_ANALYSIS': webview_an_dic['findings'],
            'APKID': apk_id,
            # end
            # 'NIAP_ANALYSIS': code_an_dic['niap'],
            # 'URLS': code_an_dic['urls'],
            # 'DOMAINS': code_an_dic['domains'],
            # 'EMAILS': code_an_dic['emails'],
            # 'STRINGS': app_dic['strings'],
            # 'FIREBASE_URLS': code_an_dic['firebase'],
            # 'FILES': app_dic['files'],
            'EXPORTED_COUNT': man_an_dic['exported_cnt'],
            # 'APKID': apk_id,
            # 'TRACKERS': trackers,
            # 'PLAYSTORE_DETAILS': app_dic['playstore'],
            'NETWORK_SECURITY': man_an_dic['network_security'],
            # 'SECRETS': app_dic['secrets'],
        }
        if update_type == 'save':
            StaticAnalyzerAndroid.objects.create(**values)
        else:
            StaticAnalyzerAndroid.objects.filter(
                MD5=app_dic['md5']).update(**values)
    except Exception:
        logger.exception('Updating DB')
    try:
        values = {
            'APP_NAME': app_dic['real_name'],
            'PACKAGE_NAME': man_data_dic['packagename'],
            'VERSION_NAME': man_data_dic['androvername'],
        }
        RecentScansDB.objects.filter(
            MD5=app_dic['md5']).update(**values)
    except Exception:
        logger.exception('Updating RecentScansDB')
