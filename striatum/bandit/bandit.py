"""
Bandit interfaces
"""
from abc import abstractmethod


# TODO: think about how to use this
class Action(object):
    """The action object"""
    @abstractmethod
    def __init__(self):
        pass


class BaseBandit(object):
    """Bandit algorithm

    Parameters
    ----------
    HistoryStorage : HistoryStorage object
        The HistoryStorage object to store history context, actions and rewards.

    ModelStorage : ModelStorage object
        The ModelStorage object to store model parameters.

    actions : list of Action objects
        List of actions to be chosen from.

    Attributes
    ----------
    HistoryStorage : HistoryStorage object
        The HistoryStorage object to store history context, actions and rewards.

    ModelStorage : ModelStorage object
        The ModelStorage object to store model parameters.

    actions : list of Action objects
        List of actions to be chosen from.
    """
    def __init__(self, HistoryStorage, ModelStorage, actions):
        self._HistoryStorage = HistoryStorage
        self._ModelStorage = ModelStorage
        self._actions = actions


    @property
    def ModelStorage(self):
        """HistoryStorage object that stores history"""
        return self._ModelStorage

    @property
    def HistoryStorage(self):
        """HistoryStorage object that stores history"""
        return self._HistoryStorage

    @property
    def actions(self):
        """List of actions"""
        return self._actions

    @abstractmethod
    def get_action(self, context):
        """Return the action to perform

        Parameters
        ----------
        context : {array-like, None}
            The context of current state, None if no context avaliable.

        Returns
        -------
        history_id : int
            The history id of the action.

        action : Actions object
            The action to perform.
        """
        pass

    @abstractmethod
    def reward(self, history_id, reward):
        """Reward the preivous action with reward.

        Parameters
        ----------
        history_id : int
            The history id of the action to reward.

        reward : float
            A float representing the feedback given to the action, the higher
            the better.
        """
        pass
