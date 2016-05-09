# Tokens for titles of data we want to extract, the data is on the line below
tokens = {
  "■予約番号": "booking_id",
  "■車両": "car",
  "■ステーション": "station",
  "■予約時間": "booking_time",
  "■利用時間": "used_time",
  "■走行距離": "distance",
  "■最高速度": "max_speed",
  "■急加速回数": "sudden_accel",
  "■急減速回数": "sudden_decel",
  "■時間料金": "time_charge",
  "■距離料金": "distance_charge",
  "■ペナルティ金額": "penalty_charge",
  "■TCP安心補償サービス": "insurance_charge",
  "■合計金額": "total_charge",
}

timesCarTrips = () ->
  trips = []
  # Find the Times Car Plus return confirmation emails
  threads = GmailApp.search('from:inquiry@plus.timescar.jp subject:返却証')
  if threads.length == 0
    Logger.log("No messages found.")
  else
    # Go through each results
    for thread in threads
      # We just want the first message in the thread
      message = thread.getMessages()[0]
      # Get the plaintext body
      body = message.getPlainBody()

      # Initialize a trip variable
      trip = {}
      # Look at each line in the email
      lines = body.split("\n")
      for i in [0..lines.length - 1]
        line = lines[i]
        # In each line, look if we find a token
        for key, token of tokens
          if line.indexOf(key) != -1
            # If a token is found, the data is on the next line so save it
            trip[token] = lines[i + 1].trim()
      trips.push(trip)
  return trips

loadTrips = () ->
  # Get the active Spreadsheet
  ss = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet()
  ss.clearContents()
  # Load the header
  header = (token for key, token of tokens)
  ss.appendRow(header)
  # Get the trips
  for trip in timesCarTrips()
    values = []
    for col in header
      values.push(trip[col])
    Logger.log(values)
    ss.appendRow(values)
