from flet import *
import random, time


def main(page:Page):
    global score    
    gc=[]
    gu=[]
    page.title='Mental Math Trainer'
    page.theme_mode='dark'

    page.bgcolor='blue'

    def check_correct(e):
        score=0
        for char in ui.value.split('\n'):
            if char.strip() in gc:
                score+=10
        m2.controls.append(
            Text(str(score))
        )
        page.update()


        print(gc)
    def lvl1(e):
        global ui
        m2.controls.clear()
        page.update()

        for i in range(2):
            en.value=str(random.randrange(1000,9999))
            page.update()
            gc.append(str(en.value))
            time.sleep(3)
            
        

        

        en.value=''
        page.update()

        cb=ElevatedButton('check',
        bgcolor='green',
        on_click=check_correct)
        m2.controls.append(cb)
        page.update()

        ui=TextField(multiline=True,
        hint_text='Enter the numbers displayed!')
        m2.controls.append(ui)
        page.update()

        

    def lvl2(e):
        global ui
        m2.controls.clear()
        page.update()

        for i in range(3):
            en.value=str(random.randrange(1000,9999))
            page.update()
            gc.append(str(en.value))
            time.sleep(3)
            
        

        

        en.value=''
        page.update()

        cb=ElevatedButton('check',
        bgcolor='green',
        on_click=check_correct)
        m2.controls.append(cb)
        page.update()

        ui=TextField(multiline=True,
        hint_text='Enter the numbers displayed!')
        m2.controls.append(ui)
        page.update()


        
        

    b1=ElevatedButton('Level 1: Training!',
    on_click=lvl1)

    b2=ElevatedButton('Level 2: Training!',
    on_click=lvl2)

    en=Text(value='')

    m2=Column(
        controls=[]
    )

    mcol=Column(
        controls=[
            Text('Train in mental math!'),
            b1,
            b2,
            en,
            m2
        ]
    )

    mrow=Row(
        alignment='center',
        controls=[
           mcol
        ]
    )


    page.add(
       
        mrow
    )

app(target=main)