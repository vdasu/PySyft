# stdlib
from typing import List
from typing import Optional
from typing import Type

# third party
from nacl.signing import VerifyKey

# relative
from ......util import traceback_and_raise
from .....common.group import VERIFYALL
from ....abstract.node import AbstractNode
from ..auth import service_auth
from ..node_service import ImmediateNodeServiceWithReply
from .get_remaining_budget_messages import GetRemainingBudgetMessage
from .get_remaining_budget_messages import GetRemainingBudgetReplyMessage


class GetRemainingBudgetService(ImmediateNodeServiceWithReply):

    @staticmethod
    @service_auth(guests_welcome=True)
    def process(
            node: AbstractNode,
            msg: GetRemainingBudgetMessage,
            verify_key: Optional[VerifyKey] = None,
    ) -> GetRemainingBudgetReplyMessage:

        if verify_key is None:
            traceback_and_raise(
                "Can't process GetRemainingBudgetService with no verification key."
            )

        try:

            result = node.acc.get_remaining_budget(user_key=verify_key, returned_epsilon_is_private=False)

            return GetRemainingBudgetReplyMessage(
                budget=result, address=msg.address
            )
        except Exception as e:
            log = (
                    f"Unable to get remaining budget for {verify_key}. "
                    + f"Possible dangling Pointer. {e}"
            )
            traceback_and_raise(Exception(log))

    @staticmethod
    def message_handler_types() -> List[Type[GetRemainingBudgetMessage]]:
        return [GetRemainingBudgetMessage]
