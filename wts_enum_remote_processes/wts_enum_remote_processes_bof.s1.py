from typing import List, Tuple

from outflank_stage1.task.base_bof_task import BaseBOFTask
from outflank_stage1.task.enums import BOFArgumentEncoding


class WTSEnumRemoteProcessesBOF(BaseBOFTask):
    def __init__(self):
        super().__init__("remote_processes", base_binary_name="wts_enum_remote_processes")

        self.parser.description = (
            "Enumerate remote processes using WTS APIs, also useful to check if you have access to a system"
        )
        self.parser.epilog = "Usage: remote_processes <host>"

        self.parser.add_argument(
            "remotehost",
            help=f"Remote host to enumerate processes of"        
        )

    def _encode_arguments_bof(
        self, arguments: List[str]
    ) -> List[Tuple[BOFArgumentEncoding, str]]:
        parser_arguments = self.parser.parse_args(arguments)

        return [(BOFArgumentEncoding.STR, parser_arguments.remotehost)]

    # def rewrite_response(self, response: Optional[str]) -> Optional[str]:
    #     return(
    #         response.replace("[+]", "\n[+]")
    #     )
    #     return (
    #         response.replace("\\Registry\\User\\", "HKEY_USERS\\")
    #         .replace("\\Registry\\Machine\\", "HKEY_LOCAL_MACHINE\\")
    #         .replace("\\REGISTRY\\USER\\", "HKEY_CURRENT_USER\\")
    #     )
