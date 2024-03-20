import copy


class Store(object):

    def __init__(self, state):
        self.state = state

    def dispatch(self, action):
        self.state = self.reducer(action)

    def reducer(self, action):
        state = copy.deepcopy(self.state)
        if action['type'] == 'increment':
            state['value'] = increment(state['value'])
        elif action['type'] == 'decrement':
            state['value'] = decrement(state['value'])
        elif action['type'] == 'increment_by_amount':
            state['value'] = increment_by_amount(state['value'], action['payload'])
        else:
            raise ValueError('Unknown action type')
        return state


def increment(value):
    return value + 1


def decrement(value):
    return value - 1


def increment_by_amount(value, amount):
    return value + amount


if __name__ == '__main__':
    store = Store({'value': 0})
    store.dispatch({'type': 'increment'})
    print(store.state)  # Output: {'value': 1}
    store.dispatch({'type': 'decrement'})
    print(store.state)  # Output: {'value': 0}
    store.dispatch({'type': 'increment_by_amount', 'payload': 5})
    print(store.state)  # Output: {'value': 5}
