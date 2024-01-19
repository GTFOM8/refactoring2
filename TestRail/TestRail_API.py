from testrail_api import TestRailAPI
from TestRail.testrail import APIClient
from environment_and_test_run import EnvAndRun as ER

from utilities.ReadProperties import ReadConfig

host = ReadConfig.get_testrail_host()
login = ReadConfig.get_testrail_login()
password = ReadConfig.get_testrail_pass()
run_id = ER.Run
send_report = True
api = TestRailAPI(host, login, password)


class TestRailAPI():
    def APItestrail(status_id, case_id):
        if send_report=="True":
            result = api.results.add_result_for_case(
                run_id=run_id,
                case_id=case_id,
                status_id=status_id,
                comment="",
                version="1"
            )
    def APItestrail_massage2(status_id, case_id, run_id, comment):
        if send_report=="True":
            result = api.results.add_result_for_case(
                run_id=run_id,
                case_id=case_id,
                status_id=status_id,
                comment=comment,
                version="1"
            )

    def APItestrail_massage3(status_id, case_id, run_id, comment):
        if send_report == "True":
            result = api.results.add_result_for_case(
                run_id=run_id,
                case_id=case_id,
                status_id=status_id,
                comment=comment,
                version="1"
            )
        # attach = file_name
        # api.attachments.add_attachment_to_result(result["id"], attach)

    def send_attach_APITestrail(self):
        client = APIClient(host)
        client.user = login
        client.password = password


def APItestrail_massage4(status_id,case_id,comment, file_name):
    if send_report=="True":
        result = api.results.add_result_for_case(
        run_id=run_id,
        case_id=case_id,
        status_id=status_id,
        comment=comment,
        version="1"
        )
        print(result)
        attach = ""
        api.attachments.add_attachment_to_result(result["id"], attach)






