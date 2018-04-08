import api from '../api';
import { COINS_FETCH_SUCCESS, COINS_FETCH_ERROR } from '../types'

export const coinsFetchSuccess = coins => ({
  type: COINS_FETCH_SUCCESS,
  payload: { coins }
});
export const coinsFetchError = error => ({
  type: COINS_FETCH_ERROR,
  payload: { error }
});

export const coinsearch = credentials => (dispatch) =>
  api.coin.coinsearch(credentials)

export const getCoins = page => dispatch => {
  api.coin.getcoins(page).then(res =>  {

    dispatch(coinsFetchSuccess(res.data.results))
    return res.data.results
  })
}

// export function getCoins() {
//   return dispatch => {
//     dispatch(coinsFetchSuccess(res.data.results))
//   }
// }
