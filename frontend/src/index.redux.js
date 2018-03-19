

const ADD_COUNT = 'addition';
const SUB_COUNT = 'subtraction';

// reducer
export function counter( state=10 , action) {
    switch (action.type){
        case 'addition':
            return state + 1;
        case 'subtraction':
            return state - 1;
        default:
            return state;
    }
}

// action creator
export function addCount() {
    return {type: ADD_COUNT}
}

export function subCount() {
    return {type: SUB_COUNT}
}

export function addCountAsync() {
    return dispatch => {
        setTimeout( () => {
            dispatch(addCount())
        },2000)
    }
}