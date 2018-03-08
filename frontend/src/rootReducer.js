import { combineReducers } from 'redux';
import user from './reducers/user'
import coins from './reducers/coins'
export default combineReducers({
  user
});
