## happy path open positions
* greet
  - utter_greet
* inform{"request_type":"job"}
  - utter_info
* inform{"role_type":"Any"}
  - action_check_positions
  - slot{"positions":[]}

# happy path application status
* inform{"request_type":"application"}
  - utter_name
  - action_check_status
  - slot{"status":"received"}
  - utter_status

## story goodbye
* goodbye
  - utter_goodbye
 