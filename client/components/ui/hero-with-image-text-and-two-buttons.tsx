import { MoveRight, PhoneCall } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import Link from "next/link";
import { pageLinks } from "@/lib/page-links";
import Image from "next/image";
import { assetsLinks } from "@/lib/assets-links";

function Hero() {
  return (
    <div className="w-full  py-20 lg:py-20 px-10">
      <div className="container mx-auto">
        <div className="grid grid-cols-1 gap-8 items-center lg:grid-cols-2">
          <div className="flex gap-4 flex-col">
            <div>
              <Badge variant="outline">We&apos;re live!</Badge>
            </div>
            <div className="flex gap-4 flex-col">
              <h1 className="text-5xl md:text-7xl max-w-lg tracking-tighter font-regular text-left">
                हर घर तक जैविक उत्पाद, हर किशन तक सही बाज़ार!
              </h1>
              <p className="text-xl leading-relaxed tracking-tight text-muted-foreground max-w-md text-left">
                JaivikSetu bridges the gap between organic farmers and conscious consumers, ensuring fair trade, purity, and trust. Scan QR codes to trace farming methods, certifications, and authenticity—bringing farm-fresh, chemical-free produce straight to you!
              </p>
            </div>
            <div className="flex flex-row gap-4">
              <Button size="lg" className="gap-4" variant="outline">
                Jump on a call <PhoneCall className="w-4 h-4" />
              </Button>
              <Link href={pageLinks.auth.signup}>
                <Button size="lg" className="gap-4">
                  Sign up here <MoveRight className="w-4 h-4" />
                </Button>
              </Link>
            </div>
          </div>
          <Image unoptimized src={assetsLinks.farmer.src} alt={assetsLinks.farmer.alt} width={0} height={0} className="h-96 w-full rounded-md object-cover" />
        </div>
      </div>
    </div>
  );
}

export { Hero };