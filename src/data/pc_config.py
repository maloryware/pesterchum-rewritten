from data.structure.pc_data import PesterchumData
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
    trusted_domains: list[str]

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
    user_idkey: str = None # imported from profile
    auto_join_memos: list[str] = [] # imported from profile

    ### hidden ###
    default_profile: str
    reveal_dev_settings: bool = False
    enable_dev_mode: bool = False

    ### --- Internal Variables --- ###
    app: Pesterchum

    def __init__(self, app: Pesterchum):

        # try to load from storage
        self.parent = app
        # if none found: load presets
        raise NotImplementedError()


    # ~ PesterchumData::save ~
    def save(self) -> None:
        raise NotImplementedError()

    # ~ PesterchumData::load ~
    def load(self) -> None:
        raise NotImplementedError()

    # ~ PesterchumData::get_dir ~
    def get_dir(self) -> str:
        raise NotImplementedError()

