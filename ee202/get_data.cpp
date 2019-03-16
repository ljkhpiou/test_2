
float my_dot(float a[6],float b[6]) {
    float result = 0;
    for(int i=0;i<6;i++){
        result = result + a[i]*b[i];
        }
    return result;
    }



vold get_command(int& cmd,float& move_x,float& move_y){

  const float coffe_0[6] = { 3.26058485e-03, -4.89987206e-03, -2.05877017e-02,  3.16671988e-03, 5.79273382e+00, -1.60204263e+00};

  const float coffe_1[6] = { 1.22703505e-03, -2.06662456e-04, -1.68982080e-02,  1.94460189e-02, -4.50079549e+00,  1.09530008e+00};

  const float coffe_2[6] = {-2.84085412e-04, -3.18166798e-03, -7.44055441e-03,  2.84450999e-02, -1.19638051e+00,  5.25903292e+00};

  const float coffe_3[6] = { 7.09153276e-03, -4.21382224e-04, -1.51337127e-02,  5.92974483e-03, 2.22769372e+00, -8.17349130e+00};

  const float bias_0 = -2.069;
  const float bias_1 = -2.005;
  const float bias_2 = -1.976;
  const float bias_3 = -2.617;

  float roll = 0;
  float pitch = 0;
  float alpha = 0.6;
  float roll_acc = 0;
  float pitch_acc = 0;
  float acc_g_x = 0; ///acceleration due to gravity
  float acc_g_y = 0;
  float accel_data[3]; // Storage for the data from the sensor
  float ax, ay;//
  float az = 10; // Integer value from the sensor to be displayed
  float gyro_data[3];  // Storage for the data from the sensor
  float gx, gy, gz; // Integer value from the sensor to be displayed
  cmd = 0;
  for (int i = 0;i<20;i++){

      accel.acquire_accel_data_g(accel_data);
      gyro.acquire_gyro_data_dps(gyro_data);

        ax = accel_data[0];
        ay = accel_data[1];
        az = accel_data[2];

        gx = gyro_data[0];
        gy = gyro_data[1];
        gz = gyro_data[2];

        roll_acc = (atan2(-ay,-az)*180.0)/M_PI;
        pitch_acc = (atan2(-ax,sqrt(ay*ay + az*az))*180.0)/M_PI;


        roll = gx*dt+roll;
        pitch = gy*dt+pitch;

        pitch = alpha*pitch+(1-alpha)*pitch_acc;
        roll = alpha*roll+(1-alpha)*roll_acc;

        acc_g_x = -cos(roll/180*M_PI)*sin(pitch/180*M_PI);
        acc_g_y = -sin(roll/180*M_PI)*cos(pitch/180*M_PI);



        ax_modify = ax - acc_g_x;
        if(abs(ax_modify) <= 0.03){
              ax_modify = 0;
              }
        ay_modify = ay - acc_g_y;
        if(abs(ay_modify) <= 0.03){
            ay_modify = 0;
            }

        ax_buffer[i] = ax_modify;
        ay_buffer[i] = ay_modify;
        roll_buffer[i] = roll;
        pitch_buffer[i] = pitch;
        gx_buffer[i] = gx;
        gy_buffer[i] = gy;

    }
    for (int i = 0;i<20;i++){
    float data_pak[6];                                                                                                                                                                           = {gx_buffer[i],gy_buffer[i],roll_buffer[i],pitch_buffer[i],ax_buffer[i],ay_buffer[i]};
        if (my_dot(data_pak,coffe_0) > -bias_0) {
            cmd = 1;
            break;
        }else if (my_dot(data_pak,coffe_1) > -bias_1) {
            cmd = 2;
            break;
        }else if (my_dot(data_pak,coffe_2) > -bias_2) {
            cmd = 3;
            break;
        }else if (my_dot(data_pak,coffe_3) > -bias_3) {
            cmd = 4;
            break;
        }
    }


    float roll_avg = 0;
    float pitch_avg = 0;
    for (int i=0;i<20;i++){
         roll_avg = roll_avg + roll_buffer[i];
         pitch_avg = pitch_avg + pitch_buffer[i];
    }
    roll_avg = roll_avg/20;
    pitch_avg = pitch_avg/20;


    move_x = 0;
    move_y = 0;

if ( roll_avg > 10) {
          move_x = roll_avg - 10;
          }
else if (roll_avg < -10) {
          move_x = roll_avg + 10;
          }
if (pitch_avg > 10) {
          move_y = pitch_avg - 10;
          }
else if (pitch_avg < -10) {
          move_y = pitch_avg + 10;
          }



}
