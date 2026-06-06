import json
from typing import Any

from data.base.pc_data import PesterchumData
from pesterchum import Pesterchum


# directory: {data}/pesterchum.json
class PesterchumConfig(PesterchumData):

    ### -- Settings --- ###

    ### chum list ###
    hide_offline_chums: bool = False
    show_empty_groups: bool = False
    show_online_chum_count: bool = False
    sort_chums: int = 0 # Alphabetically | By Mood | Manual

    ### conversations ###
    auto_idle_timer: int = 15
    show_timestamps: bool = True
    timestamp_format: int = 0 # 12hr | 24hr
    show_seconds: bool = False
    show_more_info_in_memo: bool = False
    use_animated_smilies: bool = True
    random_encounters: bool = False # imported from profile
    embed_trusted_links: list[str] = []
    mentions: list[str] = None # imported from profile
    trusted_domains: list[str] = None

    ### interface ###
    tabbed_convos: bool = True
    tabbed_memos: bool = True
    minimize_strategy: int = 0 # to taskbar | to tray | quit
    close_strategy: int = 0 # to taskbar | to tray | quit
    blink_on_message: bool = True
    blink_on_memo: bool = True

    ### sound ###
    enable_sound: bool = True
    sound_on_pester: bool = True
    sound_on_memo_msg: bool = True
    sound_on_memo_ping: bool = True
    sound_on_memo_mention: bool = True
    sound_on_honk: bool = True
    audio_device: str = "" # TODO: find out how to do audio devices
    volume: int = 100 # TODO: ditto

    ### notification ###
    enable_toasts: bool = True
    notify_on_signin: bool = True
    notify_on_signout: bool = False
    notify_on_pester: bool = True
    notify_new_convo_only: bool = True
    notify_on_mention: bool = True

    ### logging ###
    log_pesters: bool = True
    timestamp_log_pesters: bool = True
    log_memos: bool = True
    timestamp_log_memos: bool = True

    ### updates ###
    theme_repo_url: str = "https://raw.githubusercontent.com/mocchapi/pesterchum-themes/main/db.json"
    check_updates_on_start: bool = True
    notify_on_update: bool = True

    ### themes ###
    selected_theme = None # imported from profile
    pesterdunk: bool = True # imported from profile

    ### IRC ###
    irc_compat_mode: bool = False # imported from profile
    force_initials: bool = False # imported from profile
    auto_identify: bool = False # imported from profile
    auto_join_memos: list[str] = [] # imported from profile

    ### hidden ###
    default_profile: str = None
    reveal_dev_settings: bool = False
    enable_dev_mode: bool = False

    ### --- Internal Variables --- ###
    app: Pesterchum

    def __init__(self, app: Pesterchum):

        # try to load from storage
        self.parent = app
        # if none found: load presets

    # ~ PesterchumData::save ~
    def save(self) -> None:
        settings_dict: dict[str, Any] = {}

        for elem in self._build_categories():
            settings_dict[elem[0]] = elem[1]
        print(json.dumps(settings_dict, indent=4))
        # raise NotImplementedError()

    # ~ PesterchumData::load ~
    def load(self) -> None:
        raise NotImplementedError()

    # ~ PesterchumData::get_dir ~
    def get_dir(self) -> str:
        raise NotImplementedError()


    # this is very ugly, but i'm doing this absolutely exhausted,
    # at the worst time possible, with very little availability...
    # so it'll have to do.
    # open to suggestions
    # ~maloryware

    # TODO: consider `dir()`-ing it

    def _build_categories(self) -> list[tuple]:
        CHUM_LIST = ("chum_list", {
            "hide_offline_chums": self.hide_offline_chums,
            "show_empty_groups": self.show_empty_groups,
            "show_online_chum_count": self.show_online_chum_count,
            "sort_chums": self.sort_chums
        })
        CONVERSATIONS = ("conversations", {
            "auto_idle_timer": self.auto_idle_timer,
            "show_timestamps": self.show_timestamps,
            "timestamp_format": self.timestamp_format,
            "show_seconds": self.show_seconds,
            "show_more_info_in_memo": self.show_more_info_in_memo,
            "use_animated_smilies": self.use_animated_smilies,
            "random_encounters": self.random_encounters,
            "embed_trusted_links": self.embed_trusted_links,
            "mentions": self.mentions,
            "trusted_domains": self.trusted_domains
        })
        INTERFACE = ("interface", {
            "tabbed_convos": self.tabbed_convos,
            "tabbed_memos": self.tabbed_memos,
            "minimize_strategy": self.minimize_strategy,
            "close_strategy": self.close_strategy,
            "blink_on_message": self.blink_on_message,
            "blink_on_memo": self.blink_on_memo
        })
        SOUND = ("sound", {
            "enable_sound": self.enable_sound,
            "sound_on_pester": self.sound_on_pester,
            "sound_on_memo_msg": self.sound_on_memo_msg,
            "sound_on_memo_ping": self.sound_on_memo_ping,
            "sound_on_memo_mention": self.sound_on_memo_mention,
            "sound_on_honk": self.sound_on_honk,
            "audio_device": self.audio_device,
            "volume": self.volume
        })
        NOTIFICATION = ("notification", {
            "enable_toasts": self.enable_toasts,
            "notify_on_signin": self.notify_on_signin,
            "notify_on_signout": self.notify_on_signout,
            "notify_on_pester": self.notify_on_pester,
            "notify_new_convo_only": self.notify_new_convo_only,
            "notify_on_mention": self.notify_on_mention
        })
        LOGGING = ("logging", {
            "log_pesters": self.log_pesters,
            "timestamp_log_pesters": self.timestamp_log_pesters,
            "log_memos": self.log_memos,
            "timestamp_log_memos": self.timestamp_log_memos
        })
        UPDATES = ("updates", {
            "theme_repo_url": self.theme_repo_url,
            "check_updates_on_start": self.check_updates_on_start,
            "notify_on_update": self.notify_on_update
        })
        THEMES = ("themes", {
            "selected_theme": self.selected_theme,
            "pesterdunk": self.pesterdunk
        })
        IRC = ("irc", {
            "irc_compat_mode": self.irc_compat_mode,
            "force_initials": self.force_initials,
            "auto_identify": self.auto_identify,
            "auto_join_memos": self.auto_join_memos
        })
        return [CHUM_LIST, CONVERSATIONS, INTERFACE, SOUND, NOTIFICATION, LOGGING, UPDATES, THEMES, IRC]
