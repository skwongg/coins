import React from 'react';
import PropTypes from 'prop-types';
import { Form, Button, Grid, Segment } from 'semantic-ui-react';
import InlineError from '../messages/InlineError';


class CoinForm extends React.Component {

  state = {
    data: {},
    loading: false,
    errors: {}
  };

  onChange = e =>
    this.setState({
      ...this.state,
      data: { ...this.state.data, [e.target.name]: e.target.value }
    });

  onSubmit = e => {
    e.preventDefault();
    const errors = this.validate(this.state.data);
    this.setState({ errors });
    if (Object.keys(errors).length === 0) {
      this.setState({ loading: true });
    }
    console.log(this.state.data)
    console.log('loading set to true!!!!')
  }

  validate = data => {
    const errors = {};
    if (!data.quant) errors.quant = "Quantity can't be blank.";
    return errors;
  };

  render() {
    const { errors, data, loading } = this.state;

    return (
      <Segment>
        <Form onSubmit={this.onSubmit} loading={loading}>
          <Grid columns={2} stackable>
            <Grid.Row>
              <Grid.Column>
                <Form.Field error={!!errors.title}>
                  <label htmlFor="ticker">Coin Ticker</label>

                  <input
                    type="text"
                    id="quant"
                    name="quant"
                    placeholder={data.ticker}
                    value={data.ticker}
                    onChange={this.onChange}
                    />


                </Form.Field>
              </Grid.Column>
            </Grid.Row>
            <Grid.Row>
              <Button primary>Save</Button>
            </Grid.Row>
          </Grid>

        </Form>

      </Segment>


    )
  }
}

export default CoinForm
