import { USER_LOGGED_OUT } from '../types';
import api from '../api';

export const coinsearch = credentials => (dispatch) =>
  api.coin.coinsearch(credentials)
