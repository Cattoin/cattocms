from phonepe.sdk.pg.payments.v1.payment_client import PhonePePaymentClient
from phonepe.sdk.pg.env import Env
import uuid  
from phonepe.sdk.pg.payments.v1.models.request.pg_pay_request import PgPayRequest

merchant_id = "PGTESTPAYUAT"  
salt_key = "099eb0cd-02cf-4e2a-8aca-3e6c6aff0399"  
salt_index = 1 
env = Env.UAT # Change to Env.PROD when you go live

phonepe_client = PhonePePaymentClient(merchant_id=merchant_id, salt_key=salt_key, salt_index=salt_index, env=env)


unique_transaction_id = str(uuid.uuid4())[:-2]
ui_redirect_url = "samp.test/newhome"  
s2s_callback_url = "samp.test/newhome"  
amount = 100  
id_assigned_to_user_by_merchant = 'user345'  
pay_page_request = PgPayRequest.pay_page_pay_request_builder(merchant_transaction_id=unique_transaction_id,  
                                                             amount=amount,  
                                                             merchant_user_id=id_assigned_to_user_by_merchant,  
                                                             callback_url=s2s_callback_url,
redirect_url=ui_redirect_url)  
pay_page_response = phonepe_client.pay(pay_page_request)  
pay_page_url = pay_page_response.data.instrument_response.redirect_info.url