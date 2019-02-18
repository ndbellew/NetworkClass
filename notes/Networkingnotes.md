Networking Bits
===============

Speed
-----
>Electricity or light moves at 1 ft/ns (nanosecond)
>somewhere around 600 MpH.
Fiber Optics allow for the 1ft per nanosecond from 10^-6 factor to fiber optic
Sound
------
> moves at 1ft/ms

> digital moved in the block pattern but we are able to use current to reverse this however we would need to have resistors for safety

Light
-----
### Photons
>some photons created a 1
>no photons created a 0
>we could polorize the light to change the output by aligning the glass in different ways to allow more or less light in

Radio Spectrum
---------------
>Part of electromagnetic spectrum with frequencies from 3Hz to 3000 GHz
>It is a shared resource so it has been split up into different wave forms to allow the maximum amount of people to use each individual station

### Radio Waves

>*  AM and FM
   Amplitude and Frequency
   electrical field pumped from an antenna it creates a frequency that other antennas can also pick up. this was discoverd by putting two tuning forks of the same frequency on either side of a table and then ringing only one
>* Connecting antenna to antenna
   Antennas are vibrating at a rate so that it picks up specific electronic frequencies that are allowing it to have an output based on how the binary hits our machines.
   you can have antennas that are directed to specific areas that allow for optimal communication
>* 1's and 0's
   we send bursts of energy and turn the amplifier on and off to change the amplitude/Frequency which sends the binary over based solely off timing.
  Fm has higher quality and then AM had longer range, AM was the bare bones where as FM could send as high of frequency as it wanted but in order to maintain the quality it could only go so far.
>*  L+R
    Antenna submits two different 0 and 1 signals through different things
###FSK
Frequency-shift Keying
>  a frequency modulation scheme in which digital info is     transmitted through a discrete frequency, the carrier signal varies according to the digital signal changes
>>  old phone made specific tone dials we can replicate the sounds. with the right pitch you can send a call to any number even if the phone itself has no numbers.
>> simplest form is Binary
>  Frequencies change depending on what we want the phone to do.
Baud
> bits per second is what baudrate is
> to do bit frequency you would use 300 bps or 300 baud
>> eventually modems would move from 300 baud to 9600 baud and finally end at 56 Kbps or Kbaud
So we can take a wave - sine for example - and change the way that it moves (increasing frequency and decreasing amplitude).\nSo now we have a different amount in Hertz. the more we change this the more the wave appears to be a 1 to 0 transition. however this requires a high amount of bandwidth.
> to defeat this instead of getting the entire thing you send little packets at a time. and if the frequency is abovd 44 kHz it just removes those so because the human ear cannot hear that

###DOS command for Microsoft
>Dos Commands are the commands available in microsoft Dos that are used to interact with the operating system and other command line based software
>unlike in windows, Dos commands are the primary way in which you use the OS
> Windows OS does not have Dos commands. Instead the command are available from the command prompt and are called CMD Prompt commands
DOS Commands
* chdir
Displays the drive letter and folder you are currently in
* cls
clear screen
* copy
copy one or more files
* Edit
starts the MS-DOS edit or tool which is used to create and modify .txt files
* Interlnk
Used to connect two computers via a serial or parallel connection to share files and printers
* Intersvr
used to start Interlnk server and to copy Interlnk files from one computer to another
* mkdir
used to create a new directory
* MSD
Starts Microsoft Diagnostics, a tool used to display info about your computer
* path
Used to display or set a specific path available to executable files
* rmdir
used to remove directory
###Microsoft Dos Command Mode
Example: com1:9600,N,8,1,P
- Set communications port COM1 to 9600 BAud with no parity, 8 databits, 1 stop bit, and with Xon/XOFF.
Example: Mode CON: COLS=80 LINES=50
- Change the output video settings for the directory structure in DOS to 80 columns by 50 lines. When receiving error: invalid parameter -x where x is the invalid parameter the lines or cols specified is invalid setting
Example: MODE
- typing mode alone would display the current mode settings for all the ports.
> Mode status is used to view or modify a port or display setting
serial port Parameters
* COMm[:]
* BAUD=b
* PARITY=p
* DATA=d
* STOP=s
* RETRY=r

### Radio connection
> there are some locations you can find radio chips to communicate with through pi
* RS-232
defines the signals connecting between a Data Terminal Equipment (DTE) such as a computer terminal

### Network signal
Magnetic disk
- if there is a long series of 0's it will start to amplify it so that there is no long run of 0's and 1's
we can transmit a 1->0
* dont have too many 1's or 0's in a row
General picture of having more than one bit
- Startup->Sync->Data->Check->"Quiet Period"
  * Start
    - something you want to throw away like a * character
  * Sync
    - get the whole packet together and ready to send
    - how many 0's how many 1's
    - get Destination and source packets to see how and where to send them
  * DATA
    - Send the bits up until a stopping point
  * Check
    - stopping bit to check and make sure all the bits went through
  * Quiet Period
    - the stopped portion of the sending before the next one sends
this is considered the packet protocol - OSI Model
SLIP - Serial layer internet protocol
  - the original Dial Up
### RFC for SMTP
SMTP - Simple Mail Transfer Protocol
 - an internet standard for electronic mail (email)
 - this describes the process of connecting on TCP port  through a mail submission agent (MSA). The MSA delivers the mail to its mail transfer agent (MTA). the MTA uses the Domain name system (DNS) to look up th email exchanger record (MX record) for recipient's domain. the MX record holds the name of the target host. the MTA hops around the server until it finds the target and then the server either accepts it or reports failure to locate. once the final hop accepts the incoming message it hands it to the mail delivery agent (MDA) and then it delivers to the local mail server.
 - first defined by RFC 821
 - extended SMTP additions by RFC 5321. which is the protocol in widespread use today.
    -
RFC - Request for Comments
SMTP Port Number
  - 5321 is the current port used to communicate with an SMTP. a way to communicate with the server is to use the command EHLO which superseeds the earlier command HELO.
### Sending Bytes
 - Start - BITS - Parity( None, Odd Parity, Even Parity) - Stop
 2 Dimentional Parity check
NMEA
  Checking
    1. Parity - add them up to see if they are odd or even
    2. checksum + bytes - keeps 1 byte of the sum
    3. crc-64 -
  - NMEA uses checksum, meaning each process has a certain sum of data it should be and if the checksum is false it is read in as an error.
### ethernet
#### first 56 BITS
    What are they for?
### Interfaces
Spi
  - Serial Peripheral Interface
    - a synchronous serial communication - does it have a clock
#### first 56 BITSof ethernet Frame
  - Preamble and Start fram delimiter
    - The Preamble consists of a 56-bit(seven byte) pattern of alternating 1 and 0 bits.
    - This allows devices on the networks to easily synchornize their reciever clocks. providing bit-level synchonization
    - it is followed by the SFD to provide byt-level synchonization and to mark a new incoming Frame.
    - the (uncoded) on-the-wire bit pattern for the preamble together with the SFD portion of the frame is 10101010 10101010 10101010 10101010 10101010 10101010 10101010 10101011;
### Interfaces
Spi
  - Serial Peripheral Interfacesignal?
    - there are 2 devices Master and Slave and you are trying to talk as fast as possible between the 2 devices. a four wire system. most important is Ground and synchronous clock.
  - SD card
    - Most SD Cards are Spi interfaces.
