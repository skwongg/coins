import { createSelector } from 'reselect';
import { COINS_FETCH_SUCCESS, COINS_FETCH_ERROR } from '../types'

const initialState = {
  coins: [],
  error: null
}

export default function coins(state=initialState, action={}) {
  switch(action.type) {
    case COINS_FETCH_SUCCESS:
      return {
        ...state,
        coins: action.payload.coins
      };
    case COINS_FETCH_ERROR:
      return { ...state,
        error: action.payload.error,
        coins: []
      };

    default:
      return state;
  }
}

export const coinsSelector = state => state.coins;

export const allCoinsSelector = createSelector(
  coinsSelector,
  coinsHash => coinsHash ? Object.values(coinsHash) : {}
);
