import { createSelector } from 'reselect';

export default function coins(state={}, action={}) {
  switch(action.type) {
    default:
    return state;
  }
}

export const coinsSelector = state => state.coins;

export const allCoinsSelector = createSelector(
  coinsSelector,
  coinsHash => coinsHash ? Object.values(coinsHash) : {}
);
